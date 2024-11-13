import reflex as rx
from ..backend import MainState
from .. import styles


def contact_form_rows() -> rx.Component:
    return rx.vstack(
        rx.input(
            name="email",
            placeholder="Email",
            required=True,
            type="email",
            width="100%",
        ),
        rx.text_area(
            name="message",
            placeholder="Message",
            required=True,
            type="text",
            width="100%",
            height="20vh",
        ),
        rx.button(
            "Submit",
            type="submit",
            loading=MainState.loading,
            **styles.button_style,
        ),
        align="center",
    )
