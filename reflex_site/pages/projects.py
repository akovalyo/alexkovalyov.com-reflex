import reflex as rx
from typing import List
from ..templates import template
from ..navigation import routes

# from ..components.grid import *
from ..backend.state import State
from .. import styles
from ..backend.models import Project
from ..components.buttons import button


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
            rx.flex(
                rx.cond(
                    item.url,
                    button(item.url_title, item.url),
                    None,
                ),
                rx.cond(
                    item.url_secondary,
                    button(item.url_secondary_title, item.url_secondary),
                    None,
                ),
                background=f"center/cover url('{item.image}')",
                width="100%",
                height=styles.card_project_width,
                align="center",
                justify="center",
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
    )


@template(
    route=routes.PROJECTS_ROUTE,
    title="Projects",
    on_load=State.load_projects,
)
def projects() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "PROJECTS",
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
            rx.foreach(
                State.projects,
                lambda item: project_card(item),
            ),
            direction="row",
            wrap="wrap",
            spacing="6",
            justify="center",
            align="center",
        ),
        width="100%",
        align="center",
        padding_bottom="2em",
    )
