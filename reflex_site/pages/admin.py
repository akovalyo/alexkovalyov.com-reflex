import reflex as rx
from ..templates import template
from ..navigation import routes
from ..backend import (
    MainState,
    Project,
    ContactState,
    ContactMessage,
    proccess_form_data,
    get_error_message,
)
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows
from ..components import page_title
import reflex_local_auth as rxa
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
                    self.set_pending_callout("Projects uploaded", False)
        except Exception as e:
            print(get_error_message(e))
            self.set_pending_callout()
        self.loading = False
        yield
        return rx.redirect(routes.ADMIN_ROUTE)

    def load_contact_messages(self):
        try:
            with rx.session() as session:
                res = session.exec(
                    select(ContactMessage).order_by(ContactMessage.created_at)
                ).all()
                self.contact_messages = res
        except Exception as e:
            print(get_error_message(e))

    def delete_message(self, id: int):
        try:
            self.admin_loading = True
            yield
            with rx.session() as session:
                res = session.get(ContactMessage, id)
                if res:
                    session.delete(res)
                    session.commit()
                    self.set_pending_callout("Message deleted", False)
        except Exception as e:
            print(get_error_message(e))
            self.pending_callout()
        self.admin_loading = False
        yield
        return rx.redirect(routes.ADMIN_ROUTE)


def upload_projects_dialog() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                "Upload",
                color_scheme="grass",
                cursor="pointer",
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Upload Projects to Database"),
            rx.alert_dialog.description(
                "Are you sure you want to upload all projects?",
                size="2",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        cursor="pointer",
                        loading=MainState.loading,
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Upload",
                        color_scheme="grass",
                        on_click=AdminState.upload_projects,
                        cursor="pointer",
                        loading=MainState.loading,
                    ),
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )


@template(
    route=f"{routes.ADMIN_ROUTE}",
    title="Admin Panel",
    on_load=AdminState.load_contact_messages,
)
@rxa.require_login
def admin() -> rx.Component:
    return rx.vstack(
        page_title("ADMIN PANEL", padding_bottom="1em"),
        rx.heading("Messages"),
        rx.box(
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Message"),
                        rx.table.column_header_cell("Created at"),
                        rx.table.column_header_cell("Delete"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(
                        AdminState.contact_messages,
                        lambda item: rx.table.row(
                            rx.table.row_header_cell(item.email),
                            rx.table.cell(item.message),
                            rx.table.cell(
                                item.created_at,
                            ),
                            rx.table.cell(
                                rx.cond(
                                    AdminState.admin_loading,
                                    rx.spinner(),
                                    rx.icon(
                                        "trash",
                                        color="tomato",
                                        cursor="pointer",
                                        _hover={
                                            "color": styles.accent_text_color,
                                        },
                                        on_click=lambda: AdminState.delete_message(
                                            item.id
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    )
                ),
            ),
            width=styles.blog_post_content_width,
        ),
        rx.divider(),
        rx.heading("Upload Projects to Database"),
        upload_projects_dialog(),
        align="center",
        justify="center",
        width="100%",
    )
