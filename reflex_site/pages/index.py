import reflex as rx

from ..templates import template


def heading_resp() -> rx.Component:
    return rx.breakpoints(initial="4", xs="4", sm="4", md="5", lg="7", xl="7")


@template(route="/")
def index() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/main.jpg",
            width="100%",
            align="center",
            height="auto",
        ),
        rx.heading("Hello, I'm Alex.", size=heading_resp(), padding_top="1em"),
        rx.heading("I'm a software developer.", size=heading_resp()),
        width="100%",
        align="center",
    )
