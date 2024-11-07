import reflex as rx
from .. import styles


def main_button(title: str, href: str) -> rx.Component:
    return rx.link(
        rx.button(
            title,
            variant="surface",
            border_radius="10px",
            height=["35px", "35px", "40px", "50px", "50px"],
            width=["100px", "100px", "110px", "120px", "120px"],
            font_size=["1em", "1em", "1.25em", "1.4em", "1.4em"],
            font_weight="200",
            cursor="pointer",
        ),
        href=href,
    )


def button(
    title: str, href: str, padding: str = "40px", is_external: bool = False
) -> rx.Component:
    return rx.link(
        rx.button(
            title,
            variant="surface",
            border_radius="10px",
            padding=f"0 {padding}",
            cursor="pointer",
            background=styles.bar_color,
            _hover={
                # "border": "2px solid",
                "color": styles.accent_text_color,
            },
        ),
        href=href,
        is_external=is_external,
    )
