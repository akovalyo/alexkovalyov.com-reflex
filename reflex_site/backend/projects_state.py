import reflex as rx
from ..backend import Project
from typing import List
from sqlmodel import select
from ..navigation import routes
from ..backend import proccess_form_data, get_error_message, MainState
from datetime import datetime, timezone


class ProjectsState(MainState):
    projects: List["Project"] = []
    current_project: Project | None

    @rx.var(cache=True)
    def get_str_datetime_for_post(self) -> str:
        return (
            self.current_project.created_at.strftime("%Y-%m-%d")
            if self.current_project
            else ""
        )

    @rx.var(cache=True)
    def _project_id(self) -> str:
        return self.router.page.params.get("id", "")

    def clear_current_project(self):
        self.current_project = None

    def load_projects(self):
        with rx.session() as session:
            res = session.exec(
                select(Project).order_by(Project.created_at.desc())
            ).all()
            self.projects = res

    def add_project(self, form_data: dict):
        data = proccess_form_data(form_data)
        self.loading = True
        yield
        try:
            with rx.session() as session:
                db_entry = Project(**data)
                session.add(db_entry)
                session.commit()
            self.loading = False
            yield
            self.set_pending_callout("Project added", False)
            return rx.redirect(routes.PROJECTS_ROUTE)
        except Exception as e:
            print(get_error_message(e))
            self.loading = False
            yield rx.toast.error("Failed to add the project. Try again later.")

    def load_project(self):
        with rx.session() as session:
            if self._project_id == "":
                self.current_project = None
                return rx.redirect(routes.PAGE_404_ROUTE)
            res = session.get(Project, self._project_id)
            if not res:
                return rx.redirect(routes.PAGE_404_ROUTE)
            self.current_project = res

    def delete_project(self):
        self.loading = True
        yield
        try:
            with rx.session() as session:
                if self.current_project:
                    res = session.get(Project, self.current_project.id)
                    if res:
                        session.delete(res)
                        session.commit()
                        self.set_pending_callout("Project deleted", False)
        except Exception as e:
            print(get_error_message(e))
            self.set_pending_callout()
        self.clear_current_project()
        self.loading = False
        yield
        return rx.redirect(routes.PROJECTS_ROUTE)

    def cancel_delete_project(self):
        self.loading = True
        yield
        self.clear_current_project()
        self.loading = False
        yield
        return rx.redirect(routes.PROJECTS_ROUTE)
