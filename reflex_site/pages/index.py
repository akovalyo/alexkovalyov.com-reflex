import reflex as rx

from ..templates import template
from .. import styles
from ..navigation import routes
from ..components.buttons import main_button


@template(
    route=routes.HOME_ROUTE,
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
            main_button("Projects", routes.PROJECTS_ROUTE),
            main_button("Blog", routes.BLOG_ROUTE),
            padding_top="2em",
            spacing="4",
        ),
        width="100%",
        align="center",
    )
