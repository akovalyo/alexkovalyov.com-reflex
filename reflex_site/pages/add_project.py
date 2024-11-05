import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend.state import State
from .. import styles


@template(
    route=routes.ADD_PROJECT_ROUT,
    title="Add Project",
)
def add_project() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "ADD PROJECT",
                size="7",
                padding_top="1em",
                padding_bottom="0",
            ),
            rx.divider(
                height="5px",
                bg=styles.heading_color,
            ),
            gap="0",
            padding_bottom="1em",
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
                        name="url",
                        placeholder="Url",
                        required=False,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="url_title",
                        placeholder="Url Title",
                        required=False,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="url_secondary",
                        placeholder="Secondary Url",
                        required=False,
                        type="text",
                        width="100%",
                    ),
                    rx.input(
                        name="url_secondary_title",
                        placeholder="Secondary Url Title",
                        required=False,
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
                    rx.input(
                        name="created_at",
                        placeholder="Date",
                        required=False,
                        type="date",
                        width="100%",
                    ),
                    rx.button(
                        "Submit",
                        type="submit",
                    ),
                    align="center",
                ),
                on_submit=State.handle_project_submit,
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
