import reflex as rx
import reflex_local_auth as rxa
from .. import styles


def login_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/ak.png",
                    width="2.5em",
                    height="auto",
                ),
                rx.heading(
                    "Log In",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="2",
                width="100%",
            ),
            rxa.pages.login.login_error(),
            rx.text("Username"),
            rx.input(
                rx.input.slot(rx.icon("user")),
                placeholder="Username",
                type="email",
                id="username",
                name="username",
                size="3",
                width="100%",
            ),
            rx.text("Password"),
            rx.input(
                rx.input.slot(rx.icon("lock")),
                placeholder="Password",
                type="password",
                id="password",
                name="password",
                size="3",
                width="100%",
            ),
            rx.button("Sign in", width="100%"),
            width=styles.form_max_width,
        ),
        on_submit=rxa.login.LoginState.on_submit,
    )
