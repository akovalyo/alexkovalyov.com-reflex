import reflex as rx

import reflex_local_auth as rxa
from ..navigation import routes
from ..templates import template
from ..forms.login_form import login_form


@template(
    route=routes.LOGIN_ROUTE,
    title="Log In",
)
def login() -> rx.Component:
    return rx.vstack(
        rx.cond(
            rxa.LoginState.is_hydrated,  # type: ignore
            rx.card(
                login_form(),
            ),
        ),
        padding_top="4em",
        width="100%",
        align="center",
    )
