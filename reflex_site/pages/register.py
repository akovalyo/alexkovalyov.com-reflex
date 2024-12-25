import reflex as rx

import reflex_local_auth as rxa
from ..navigation import routes
from ..templates import template
from ..forms.register_form import register_form


@template(
    route=routes.REGISTER_ROUTE,
    title="Register",
)
def register() -> rx.Component:
    return rx.vstack(
        rx.cond(
            rxa.LoginState.is_hydrated,  # type: ignore
            rx.card(
                register_form(),
            ),
        ),
        padding_top="4em",
        width="100%",
        align="center",
    )
