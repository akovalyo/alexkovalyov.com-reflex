import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend.state import BlogPostState
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows


@template(
    route=routes.ADD_BLOG_POST_ROUT,
    title="Add Blog Post",
    on_load=BlogPostState.clear_current_blog_post,
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
                height="5px",
                bg=styles.heading_color,
            ),
            gap="0",
            padding_bottom="1em",
            align="center",
        ),
        rx.box(
            rx.form(
                blog_post_form_rows(),
                on_submit=BlogPostState.add_blog_post,
                reset_on_submit=True,
            ),
            width=styles.form_max_width,
        ),
        align="center",
        justify="center",
        width="100%",
    )
