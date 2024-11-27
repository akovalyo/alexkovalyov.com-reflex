import reflex as rx

from . import styles
from .pages import *
from .components import navbar, sidebar
from .backend import ThemeState
from .pages.page404 import page404_content

app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    overlay_component=rx.toast.provider(close_button=True),
)
app.add_custom_404_page(
    rx.theme(
        rx.flex(
            navbar(),
            sidebar(),
            rx.flex(
                page404_content(),
                width="100%",
            ),
            flex_direction=[
                "column",
                "column",
                "column",
                "column",
                "column",
                "row",
            ],
            width="100%",
            margin="auto",
            position="relative",
        ),
        has_background=True,
        accent_color=ThemeState.accent_color,
        gray_color=ThemeState.gray_color,
        radius=ThemeState.radius,
        scaling=ThemeState.scaling,
    )
)
