import reflex as rx
from typing import List
from ..backend.state import Blog, Project
from .. import styles


def project_card(item: Project) -> rx.Component:

    return rx.box(
        rx.vstack(
            rx.box(
                rx.text(
                    item.title,
                    align="center",
                ),
                width="100%",
                padding="5px 0",
            ),
            rx.box(
                "",
                background=f"center/cover url('{item.image}')",
                width="100%",
                height=styles.card_project_width,
            ),
            rx.flex(
                rx.text(
                    item.description,
                    align="center",
                ),
                width="100%",
                padding="5px",
                height="60px",
                align="center",
                justify="center",
            ),
            height="100%",
            gap="0",
            bg=styles.bar_color,
            border_radius="13px",
        ),
        width=styles.card_project_width,
        height="auto",
        border=styles.border,
        border_radius="15px",
        _hover={
            "border_color": styles.accent_text_color,
            "opacity": 0.8,
        },
    )


def blog_card(item: Blog) -> rx.Component:
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


def grid(items: List[Blog] | List[Project]) -> rx.Component:
    return rx.flex(
        rx.foreach(
            items,
            lambda item: rx.cond(
                item.category == "project", project_card(item), blog_card(item)
            ),
        ),
        direction="row",
        wrap="wrap",
        spacing="6",
        justify="center",
        align="center",
    )
