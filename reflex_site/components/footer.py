import reflex as rx
from datetime import datetime


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", "https://github.com/akovalyo"),
        social_link("linkedin", "https://www.linkedin.com/in/alexandrkovalyov/"),
        social_link("instagram", "https://www.instagram.com/akovalyo/"),
        spacing="3",
        padding="1em",
        justify_content="center",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.center(
            rx.vstack(
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
                    spacing="2",
                    align="center",
                ),
                rx.text(
                    f"Copyright Alex Kovalyov © {datetime.now().year}",
                    white_space="nowrap",
                    weight="light",
                    size="2",
                ),
                justify_content="center",
                spacing="0",
                align="center",
            ),
        ),
        width="100%",
    )
