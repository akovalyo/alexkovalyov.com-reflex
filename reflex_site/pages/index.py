import reflex as rx

from ..templates import template
from .. import styles
from ..navigation import routes
from ..components import button
from ..components import page_title
from ..forms.contact_form import contact_form_rows
from ..backend import ContactState
from ..backend import HomePageState
from ..components import project_card, blog_card


def project_tiles_loading() -> rx.Component:
    return rx.flex(
        rx.skeleton(
            rx.box(
                width=styles.card_project_width,
                height="400px",
                border=styles.border,
                border_radius="15px",
            ),
        ),
        rx.skeleton(
            rx.box(
                width=styles.card_project_width,
                height="400px",
                border=styles.border,
                border_radius="15px",
            ),
        ),
        rx.skeleton(
            rx.box(
                width=styles.card_project_width,
                height="400px",
                border=styles.border,
                border_radius="15px",
            ),
        ),
        direction="row",
        wrap="wrap",
        spacing="6",
        justify="center",
        align="center",
    )


def blog_post_tiles_loading() -> rx.Component:
    return rx.flex(
        rx.skeleton(
            rx.box(
                width=styles.card_blog_width,
                height="200px",
                border=styles.border,
                border_radius="15px",
            ),
        ),
        rx.skeleton(
            rx.box(
                width=styles.card_blog_width,
                height="200px",
                border=styles.border,
                border_radius="15px",
            ),
        ),
        direction="row",
        wrap="wrap",
        spacing="6",
        justify="center",
        align="center",
    )


@template(
    route=routes.HOME_ROUTE,
    title="Home",
    on_load=HomePageState.load_data_for_home_page,
)
def index() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/main.jpg",
            width="100%",
            align="center",
            height="auto",
        ),
        rx.vstack(
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
                page_title("PROJECTS", padding_bottom="1em", padding_top="2em"),
                rx.cond(
                    HomePageState.loading,
                    project_tiles_loading(),
                    rx.flex(
                        rx.foreach(
                            HomePageState.latest_projects,
                            lambda item: project_card(item),
                        ),
                        direction="row",
                        wrap="wrap",
                        spacing="6",
                        justify="center",
                        align="center",
                    ),
                ),
                button("All", routes.PROJECTS_ROUTE),
                rx.divider(),
                page_title("BLOG", padding_bottom="1em"),
                rx.cond(
                    HomePageState.loading,
                    blog_post_tiles_loading(),
                    rx.flex(
                        rx.foreach(
                            HomePageState.latest_blog_posts,
                            lambda item: blog_card(item),
                        ),
                        direction="row",
                        wrap="wrap",
                        spacing="6",
                        justify="center",
                        align="center",
                    ),
                ),
                button("All", routes.BLOG_ROUTE),
                rx.divider(),
                page_title("CONTACT", padding_bottom="1em"),
                rx.box(
                    rx.form(
                        contact_form_rows(),
                        on_submit=ContactState.handle_submit,
                        reset_on_submit=True,
                    ),
                    width=styles.form_max_width,
                ),
                spacing="4",
                align="center",
            ),
            width="90%",
            align="center",
        ),
        width="100%",
        align="center",
    )
