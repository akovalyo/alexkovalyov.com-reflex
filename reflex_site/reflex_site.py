import reflex as rx

from rxconfig import config


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
