import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend import ProjectsState
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows
import reflex_local_auth as rxa


@template(
    route=f"{routes.PROJECTS_ROUTE}/[id]/delete",
    title="Delete Project",
    on_load=ProjectsState.load_project,
)
@rxa.require_login
def delete_project() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "DELETE PROJECT",
                size="7",
                padding_top="1em",
                padding_bottom="0",
            ),
            rx.divider(
                height="5px",
                bg=styles.heading_color,
            ),
            gap="0",
            padding_bottom="1em",
            # width="100%",
            align="center",
        ),
        rx.vstack(
            rx.cond(
                ProjectsState.current_project,
                rx.text(
                    f"Are you sure you want to delete project '{ProjectsState.current_project.title}'?"
                ),
                None,
            ),
            rx.hstack(
                rx.button(
                    "Yes",
                    on_click=ProjectsState.delete_project,
                    cursor="pointer",
                ),
                rx.button(
                    "No",
                    on_click=ProjectsState.cancel_delete_project,
                    background=styles.green_color,
                    cursor="pointer",
                ),
                width="100%",
                justify="center",
            ),
            # width="100%",
        ),
        align="center",
        justify="center",
        width="100%",
    )
