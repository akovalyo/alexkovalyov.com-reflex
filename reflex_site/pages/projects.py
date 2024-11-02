import reflex as rx

from ..templates import template
from ..navigation import routes


@template(
    route=routes.PROJECTS_ROUTE,
    title="Projects",
)
def projects() -> rx.Component:
    return rx.vstack(
        rx.heading("Projects", size="5", padding_top="2em"),
        width="100%",
        align="center",
    )
