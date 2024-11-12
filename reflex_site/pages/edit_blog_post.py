import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend import BlogPostState
from .. import styles
from ..forms.blog_post_form import blog_post_form_rows
from ..components import page_title, alert_dialog
import reflex_local_auth as rxa


@template(
    route=f"{routes.BLOG_ROUTE}/[address]/edit",
    title="Edit Blog Post",
    on_load=BlogPostState.get_blog_post,
)
@rxa.require_login
def edit_blog_post() -> rx.Component:
    return rx.vstack(
        page_title("EDIT BLOG POST", padding_bottom="1em"),
        alert_dialog(),
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
