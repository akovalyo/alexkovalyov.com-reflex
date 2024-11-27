import reflex as rx

from ..templates import template
from ..navigation import routes


def page404_content():
    return rx.vstack(
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
        gap="0",
        justify="center",
        align="center",
        height="100%",
        width="100%",
    )


@template(
    route=routes.PAGE_404_ROUTE,
    title="404",
)
def page404() -> rx.Component:
    return page404_content()
