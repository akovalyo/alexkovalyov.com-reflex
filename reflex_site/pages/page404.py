import reflex as rx

from ..templates import template
from ..navigation import routes
from ..components.grid import *
from ..backend.state import State
from .. import styles


@template(
    route="/404",
    title="404",
)
def page404() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.spacer(),
            rx.vstack(
                rx.heading(
                    "404",
                    size="7",
                    padding_bottom="5px",
                    align="center",
                    text_align="center",
                    width="100%",
                ),
                rx.divider(
                    width="100%",
                    height="1px",
                ),
                rx.heading(
                    "This page could not be found.",
                    size="4",
                    font_weight="300",
                    padding_top="5px",
                ),
            ),
            rx.spacer(),
            gap="0",
        ),
        width="100%",
        height="100%",
    )
