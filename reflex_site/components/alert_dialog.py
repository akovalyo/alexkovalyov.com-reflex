import reflex as rx
from ..backend import BlogPostState


def alert_dialog() -> rx.Component:
    return rx.alert_dialog.root(
        rx.alert_dialog.trigger(
            rx.button(
                "Delete",
                color_scheme="tomato",
                cursor="pointer",
            ),
        ),
        rx.alert_dialog.content(
            rx.alert_dialog.title("Delete Blog Post"),
            rx.alert_dialog.description(
                "Are you sure you want to delete this blog post?",
                size="2",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        cursor="pointer",
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Delete",
                        color_scheme="tomato",
                        on_click=BlogPostState.delete_blog_post,
                        cursor="pointer",
                    ),
                ),
                spacing="3",
                justify="end",
            ),
            style={"max_width": 500},
        ),
    )
