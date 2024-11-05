import reflex as rx

from ..templates import template
from ..navigation import routes
from ..components.grid import *
from ..backend.state import State
from .. import styles


@template(
    route="/blog/[address]",
    title="Blog",
)
def post() -> rx.Component:
    return (
        rx.vstack(
            rx.heading(
                f"BLOG {rx.State.address}",
                size="7",
                padding_top="2em",
                padding_bottom="0",
            ),
            rx.divider(
                width="100%",
                height="5px",
                bg=styles.heading_color,
            ),
            rx.text(
                "",
            ),
            gap="0",
            padding_bottom="1em",
        ),
    )
