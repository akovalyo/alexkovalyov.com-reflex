import reflex as rx
from ..templates import template
from ..navigation import routes
from ..backend import (
    MainState,
    Project,
    ContactState,
    ContactMessage,
    AdminState,
    proccess_form_data,
    get_error_message,
)
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows
from ..components import page_title
import reflex_local_auth as rxa
from ..db.db import db_projects
from sqlmodel import select


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
            rx.alert_dialog.title("Upload Projects to the Database"),
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


def upload_blog_dialog() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                "Upload",
                color_scheme="grass",
                cursor="pointer",
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Upload Blog Posts to the Database"),
            rx.alert_dialog.description(
                "Are you sure you want to upload all blog posts?",
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
                        on_click=AdminState.upload_blog,
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
        rx.heading("Upload Projects to the  Database"),
        upload_projects_dialog(),
        rx.divider(),
        rx.heading("Upload Blog Posts to the Database"),
        upload_blog_dialog(),
        align="center",
        justify="center",
        width="100%",
    )
