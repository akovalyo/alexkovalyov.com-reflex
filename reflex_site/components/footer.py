import reflex as rx
from datetime import datetime

from .socials import socials


def footer() -> rx.Component:
    return rx.vstack(
        socials(),
        rx.hstack(
            rx.text(
                "Built with",
                size="2",
                weight="light",
            ),
            rx.link(
                rx.image(
                    src="/reflex_logo.jpg",
                    width="1em",
                    height="auto",
                    border_radius="25%",
                ),
                href="https://reflex.dev",
            ),
            justify_content="center",
            width="100%",
        ),
        rx.text(
            f"Copyright Alex Kovalyov © {datetime.now().year}",
            white_space="nowrap",
            weight="light",
            size="2",
        ),
        width="100%",
        justify_content="center",
        spacing="0",
        align="center",
    )
