import reflex as rx
from .. import styles


def main_button(title: str, href: str) -> rx.Component:
    return rx.link(
        rx.button(
            title,
            **styles.main_button_style,
        ),
        href=href,
    )


def button(
    title: str, href: str, padding: str = "40px", is_external: bool = False
) -> rx.Component:
    return rx.link(
        rx.button(
            title,
            padding=f"0 {padding}",
            **styles.button_style,
        ),
        href=href,
        is_external=is_external,
    )
