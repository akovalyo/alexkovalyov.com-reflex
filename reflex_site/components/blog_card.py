import reflex as rx
from .. import styles
from ..backend import BlogPost
from ..navigation import routes


def blog_card(item: BlogPost) -> rx.Component:
    return rx.link(
        rx.box(
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
                        color=styles.text_color,
                    ),
                    rx.text(
                        item.description,
                        align="center",
                        size="3",
                        font_weight="100",
                        color=styles.text_color,
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
            },
        ),
        href=f"{routes.BLOG_ROUTE}/{item.address}",
        underline="none",
    )
