import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend.state import State
from ..backend.models import BlogPost
from .. import styles


def blog_card(item: BlogPost) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(
                src=item.image,
                width="100%",
                border_radius="13px 13px 0 0",
                height=styles.card_blog_height,
                object_fit="cover",
            ),
            rx.flex(
                rx.heading(
                    item.title,
                    align="center",
                    size="4",
                    padding_bottom="5px",
                ),
                rx.text(
                    item.description,
                    align="center",
                    size="3",
                    font_weight="100",
                ),
                direction="column",
                width="100%",
                padding="5px",
                height="auto",
                align="center",
                justify="center",
                bg=styles.bar_color,
                border_radius="0 0 13px 13px",
            ),
            height="100%",
            gap="0",
        ),
        width=styles.card_blog_width,
        height="auto",
        border=styles.border,
        border_radius="15px",
        _hover={
            "border_color": styles.accent_text_color,
            "opacity": 0.8,
        },
    )


@template(
    route=routes.BLOG_ROUTE,
    title="Blog",
    on_load=State.load_blog_posts,
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
            gap="0",
            padding_bottom="1em",
        ),
        rx.flex(
            rx.foreach(State.blog_posts, lambda item: blog_card(item)),
            direction="row",
            wrap="wrap",
            spacing="6",
            justify="center",
            align="center",
        ),
        width="100%",
        align="center",
    )
