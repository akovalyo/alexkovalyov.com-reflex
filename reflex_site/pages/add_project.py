import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend import ProjectsState
from ..forms.project_form import project_form_rows
from .. import styles


@template(
    route=routes.ADD_PROJECT_ROUT,
    title="Add Project",
    on_load=ProjectsState.clear_current_project,
)
def add_project() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "ADD PROJECT",
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
            align="center",
        ),
        rx.box(
            rx.form(
                project_form_rows(),
                on_submit=ProjectsState.add_project,
                reset_on_submit=True,
            ),
            width=[
                "75vw",
                "65vw",
                "55vw",
                "45vw",
                "35vw",
            ],
        ),
        align="center",
        justify="center",
        width="100%",
    )
