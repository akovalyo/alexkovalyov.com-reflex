import reflex as rx

from ..templates import template
from ..navigation import routes
from ..components.grid import *
from ..backend.state import State
from .. import styles
from ..backend.state import State


@template(
    route=routes.ADD_BLOG_POST_ROUT,
    title="Add Blog Post",
)
def add_blog_post() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "ADD BLOG POST",
                size="7",
                padding_top="1em",
                padding_bottom="0",
            ),
            rx.divider(
                # width="100%",
                height="5px",
                bg=styles.heading_color,
            ),
            gap="0",
            padding_bottom="1em",
            # width="100%",
            align="center",
        ),
        rx.box(
            rx.form(
                rx.vstack(
                    rx.input(
                        name="title",
                        placeholder="Title",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="description",
                        placeholder="Description",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="image",
                        placeholder="Image link",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.text_area(
                        name="content",
                        placeholder="Content",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="created_at",
                        placeholder="Date",
                        required=False,
                        type="date",
                        width="100%",
                    ),
                    rx.input(
                        name="address",
                        placeholder="Address",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.button(
                        "Submit",
                        type="submit",
                    ),
                    align="center",
                ),
                on_submit=State.handle_blog_post_submit,
                reset_on_submit=True,
            ),
            width=[
                "75vw",
                "65vw",
                "55vw",
                "45vw",
                "35vw",
            ],
        ),
        align="center",
        justify="center",
        width="100%",
    )
