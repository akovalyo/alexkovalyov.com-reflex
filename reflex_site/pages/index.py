import reflex as rx


@rx.page(
    "/",
    title="Alex Kovalyov",
    description="Personal site",
)
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.logo(),
    )
