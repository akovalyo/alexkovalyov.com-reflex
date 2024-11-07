import reflex as rx
from typing import List
from ..templates import template
from ..navigation import routes

from ..components.title import page_title
from ..backend.state import ProjectsState
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
            rx.box(
                background=f"center/cover url('{item.image}')",
                width="100%",
                height=styles.card_project_width,
            ),
            rx.flex(
                rx.text(
                    item.description,
                    align="center",
                    padding_bottom="10px",
                ),
                rx.spacer(gap="0"),
                rx.cond(
                    item.url,
                    rx.box(
                        button(
                            item.url_title,
                            item.url,
                            is_external=True,
                        ),
                        padding_bottom="10px",
                    ),
                    None,
                ),
                rx.cond(
                    item.url_secondary,
                    button(
                        item.url_secondary_title,
                        item.url_secondary,
                        is_external=True,
                    ),
                    None,
                ),
                direction="column",
                width="100%",
                padding="5px",
                height="150px",
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
    on_load=ProjectsState.load_projects,
)
def projects() -> rx.Component:
    return rx.vstack(
        page_title("PROJECTS", padding_top="2em", padding_bottom="1em"),
        rx.flex(
            rx.foreach(
                ProjectsState.projects,
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
