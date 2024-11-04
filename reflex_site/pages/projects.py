import reflex as rx

from ..templates import template
from ..navigation import routes
from ..components.grid import *
from ..backend.state import State
from .. import styles


@template(
    route=routes.PROJECTS_ROUTE,
    title="Projects",
    on_load=State.load_projects,
)
def projects() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "PROJECTS",
                size="7",
                padding_top="2em",
                padding_bottom="0",
            ),
            rx.divider(
                width="100%",
                height="5px",
                bg=styles.heading_color,
            ),
            id="test",
            gap="0",
        ),
        grid(State.projects),
        width="100%",
        align="center",
    )
