import reflex as rx
from .. import styles


def page_title(
    title: str,
    padding_top: str = "1em",
    padding_bottom: str = "0",
) -> rx.Component:
    return (
        rx.vstack(
            rx.heading(
                title,
                size="7",
                padding_bottom="0",
                text_align="center",
                font_weight="500",
            ),
            rx.divider(
                width="100%",
                height="5px",
                bg=styles.heading_color,
            ),
            gap="0",
            padding_top=padding_top,
            padding_bottom=padding_bottom,
        ),
    )
