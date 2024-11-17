import reflex as rx
from ..navigation import routes
from ..backend import (
    MainState,
    Project,
    ContactMessage,
    proccess_form_data,
    get_error_message,
)
from ..db.db import db_projects
from sqlmodel import select


class AdminState(MainState):
    contact_messages: list[ContactMessage] = []
    admin_loading: bool = False

    def upload_projects(self):
        self.loading = True
        yield
        try:
            with rx.session() as session:
                for item in db_projects:
                    data = proccess_form_data(item)
                    db_entry = Project(**data)
                    session.add(db_entry)
                    session.commit()
            self.loading = False
            yield rx.toast.success("Projects uploaded")
        except Exception as e:
            print(get_error_message(e))
            self.loading = False
            yield rx.toast.error("Something went wrong.")

    def load_contact_messages(self):
        try:
            with rx.session() as session:
                res = session.exec(
                    select(ContactMessage).order_by(ContactMessage.created_at)
                ).all()
                self.contact_messages = res
        except Exception as e:
            print(get_error_message(e))
            yield rx.toast.error("Something went wrong.")

    def delete_message(self, id: int):
        try:
            self.admin_loading = True
            yield
            with rx.session() as session:
                res = session.get(ContactMessage, id)
                if res:
                    session.delete(res)
                    session.commit()
            self.admin_loading = False
            yield
            self.set_pending_callout("Message deleted", False)
            return rx.redirect(routes.ADMIN_ROUTE)
        except Exception as e:
            print(get_error_message(e))
            self.admin_loading = False
            yield rx.toast.error("Something went wrong.")
