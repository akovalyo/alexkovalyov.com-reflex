import reflex as rx

from rxconfig import config
from . import styles
from .pages import *


app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    title="Alex Kovalyov",
    description="Personal site",
)
