import reflex as rx

from ..templates import template
from .. import styles


def main_button(title: str, href: str) -> rx.Component:
    return rx.button(
        title,
        variant="surface",
        radius="full",
        on_click=rx.redirect(href),
        cursor="pointer",
        height=["35px", "35px", "40px", "50px", "50px"],
        width=["100px", "100px", "110px", "120px", "120px"],
        font_size=["1em", "1em", "1.25em", "1.4em", "1.4em"],
        font_weight="200",
    )


@template(
    route="/",
    title="Home",
)
def index() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/main.jpg",
            width="100%",
            align="center",
            height="auto",
        ),
        rx.heading(
            "Hello, I'm Alex.",
            font_size=styles.main_page_font_size,
            font_weight="400",
            padding_top="1em",
        ),
        rx.heading(
            "I'm a software developer.",
            font_size=styles.main_page_font_size,
            font_weight="400",
        ),
        rx.vstack(
            main_button("Projects", "/projects"),
            main_button("Blog", "/projects"),
            padding_top="2em",
            spacing="4",
        ),
        width="100%",
        align="center",
    )
