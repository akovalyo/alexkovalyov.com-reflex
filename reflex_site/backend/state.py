import reflex as rx
from ..backend.models import BlogPost, Project
from typing import List
from sqlmodel import select
from ..backend.utils import (
    convert_datetime_to_str,
    add_datetime_to_form_data,
)
from ..navigation import routes


class State(rx.State):
    latest_blog_posts: List["BlogPost"] = []
    latest_projects: List["Project"] = []

    def load_data_for_home_page(self):
        # load latest blogs and projects
        pass


class BlogPostState(State):
    blog_posts: List["BlogPost"] = []
    blog_post: BlogPost | None
    blog_post_is_loading: bool = True

    @rx.var(cache=True)
    def _blog_post_address(self):
        return self.router.page.params.get("address", "")

    @rx.var
    def get_str_datetime(self) -> str:
        return (
            convert_datetime_to_str(self.blog_post.created_at) if self.blog_post else ""
        )

    def get_empty_blog_post(self) -> BlogPost:
        return BlogPost(
            id=None,
            title="",
            description="",
            image="",
            content="",
            created_at="",
            address="",
        )

    def clear_current_blog_post(self):
        self.blog_post = self.get_empty_blog_post()

    def update_content_value(self, value):
        self.blog_post.content = value

    def load_blog_posts(self):
        with rx.session() as session:
            # session.exec(select(BlogPost).order_by(BlogPost.created_at.desc()).limit(4)).all()
            res = session.exec(select(BlogPost)).all()
            self.blog_posts = res

    def get_blog_post(self):
        self.blog_post_is_loading = True
        with rx.session() as session:
            if self._blog_post_address == "":
                self.blog_post = None
                return rx.redirect(routes.PAGE_404_ROUTE)
            res = session.exec(
                select(BlogPost).where(BlogPost.address == self._blog_post_address)
            ).one_or_none()
            if not res:
                return rx.redirect(routes.PAGE_404_ROUTE)
            self.blog_post = res
            self.blog_post_is_loading = False

    def add_blog_post(self, form_data: dict):
        data = add_datetime_to_form_data(form_data)
        with rx.session() as session:
            db_entry = BlogPost(**data)
            session.add(db_entry)
            session.commit()
        self.clear_current_blog_post()
        return rx.redirect(routes.BLOG_ROUTE)

    def edit_blog_post(self, form_data: dict):
        data = add_datetime_to_form_data(form_data)
        with rx.session() as session:
            res = session.get(BlogPost, self.blog_post.id)
            if res:
                for k, v in data.items():
                    setattr(res, k, v)
            else:
                # TODO Change to show the error message
                return rx.redirect("/404")
            session.add(res)
            session.commit()
            return rx.redirect(f"{routes.BLOG_ROUTE}/{self.blog_post.address}")


class ProjectsState(State):
    projects: List["Project"] = []

    def load_projects(self):
        with rx.session() as session:
            res = session.exec(select(Project)).all()
            self.projects = res

    def handle_project_submit(self, form_data: dict):
        data = add_datetime_to_form_data(form_data)
        with rx.session() as session:
            db_entry = Project(**data)
            session.add(db_entry)
            session.commit()
