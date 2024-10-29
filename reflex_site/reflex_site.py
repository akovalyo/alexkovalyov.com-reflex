import reflex as rx

from rxconfig import config
from . import styles
from .pages import *


app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    html_lang="en",
    theme=rx.theme(
        appearance="inherit",
        accent_color="tomato",
    ),
)
