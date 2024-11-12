import reflex as rx
from .. import styles
from ..backend.models import Project
from ..components import button
from ..navigation import routes
import reflex_local_auth as rxa


def project_card(item: Project) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    item.title,
                    align="center",
                ),
                rx.cond(
                    rxa.LocalAuthState.is_authenticated,
                    rx.icon(
                        "trash-2",
                        size=18,
                        color=rx.color("accent"),
                        cursor="pointer",
                        _hover={
                            "color": styles.accent_text_color,
                        },
                        on_click=lambda: rx.redirect(
                            f"/{routes.PROJECTS_ROUTE}/{item.id}/delete"
                        ),
                    ),
                    None,
                ),
                width="100%",
                padding="5px 0",
                align="center",
                justify="center",
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
