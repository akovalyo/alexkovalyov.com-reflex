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
                height=styles.card_height,
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
        ),
        width=styles.card_width,
        height="auto",
        border=styles.border,
        border_radius="var(--radius-4)",
        _hover={
            "border_color": styles.accent_text_color,
            "opacity": 0.8,
        },
    )


def blog_card(item: Blog) -> rx.Component:
    return rx.box()


def grid(items: List[Blog] | List[Project]) -> rx.Component:
    return rx.flex(
        rx.foreach(
            items,
            lambda item: rx.cond(
                item.type == "project", project_card(item), blog_card(item)
            ),
        ),
        direction="row",
        wrap="wrap",
        spacing="6",
        justify="center",
        align="center",
    )
