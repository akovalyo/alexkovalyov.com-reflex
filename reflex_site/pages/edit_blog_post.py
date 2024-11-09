import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend.state import BlogPostState
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows


@template(
    route="/blog/[address]/edit",
    title="Edit Blog Post",
    on_load=BlogPostState.get_blog_post,
)
def edit_blog_post() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "EDIT BLOG POST",
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
                blog_post_form_rows(),
                on_submit=BlogPostState.edit_blog_post,
            ),
            width=styles.form_max_width,
        ),
        align="center",
        justify="center",
        width="100%",
    )
