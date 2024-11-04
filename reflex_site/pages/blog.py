import reflex as rx

from ..templates import template
from ..navigation import routes
from ..components.grid import *
from ..backend.state import State
from .. import styles


@template(
    route=routes.BLOG_ROUTE,
    title="Blog",
    on_load=State.load_blog,
)
def blog() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "BLOG",
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
            padding_bottom="1em",
        ),
        grid(State.blog),
        width="100%",
        align="center",
    )
