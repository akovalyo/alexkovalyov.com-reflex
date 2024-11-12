import reflex as rx
from ..templates import template
from ..navigation import routes

from ..components import page_title
from ..backend import ProjectsState
from ..components import project_card


@template(
    route=routes.PROJECTS_ROUTE,
    title="Projects",
    on_load=ProjectsState.load_projects,
)
def projects() -> rx.Component:
    return rx.vstack(
        page_title("PROJECTS", padding_top="2em", padding_bottom="1em"),
        rx.flex(
            rx.foreach(
                ProjectsState.projects,
                lambda item: project_card(item),
            ),
            direction="row",
            wrap="wrap",
            spacing="6",
            justify="center",
            align="center",
        ),
        width="100%",
        align="center",
        padding_bottom="2em",
    )
