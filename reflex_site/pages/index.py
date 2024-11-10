import reflex as rx

from ..templates import template
from .. import styles
from ..navigation import routes
from ..components.buttons import button
from ..components.title import page_title
from ..forms.contact_form import contact_form_rows
from ..backend.contact_state import ContactState


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
            page_title("PROJECTS", padding_bottom="1em"),
            button("More", routes.PROJECTS_ROUTE),
            page_title("BLOG", padding_bottom="1em"),
            button("More", routes.BLOG_ROUTE),
            # padding_top="2em",
            spacing="4",
            align="center",
        ),
        rx.vstack(
            page_title("CONTACT", padding_bottom="1em"),
        ),
        rx.box(
            rx.form(
                contact_form_rows(),
                on_submit=ContactState.handle_submit,
                reset_on_submit=True,
            ),
            width=styles.form_max_width,
        ),
        width="100%",
        align="center",
    )
