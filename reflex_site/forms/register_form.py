import reflex as rx
import reflex_local_auth as rxa
from .. import styles
from ..backend import AuthState


def register_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/ak.png",
                    width="2.5em",
                    height="auto",
                ),
                rx.heading(
                    "Create an account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="2",
                width="100%",
            ),
            rxa.pages.registration.register_error(),
            rx.text("Username"),
            rxa.pages.components.input_100w("username"),
            rx.text("Password"),
            rxa.pages.components.input_100w("password", type="password"),
            rx.text("Confirm Password"),
            rxa.pages.components.input_100w("confirm_password", type="password"),
            rx.text("Registration Code"),
            rxa.pages.components.input_100w("code", type="password"),
            rx.button("Sign up", width="100%"),
            width=styles.form_max_width,
        ),
        on_submit=AuthState.handle_registration,
    )
