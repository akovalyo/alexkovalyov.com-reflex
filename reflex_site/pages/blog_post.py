import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend.state import BlogPostState
from .. import styles
from ..components.title import page_title
from ..components.buttons import button


def blog_post_loading() -> rx.Component:
    return rx.vstack(
        rx.skeleton(
            rx.box(
                width="100%",
                height="40vh",
            ),
        ),
        rx.skeleton(
            rx.box(
                width=styles.form_max_width,
                height="60px",
            ),
            margin_top="1em",
        ),
        rx.skeleton(
            rx.box(
                width=styles.form_max_width,
                height="25vh",
            ),
            margin_top="1em",
        ),
        width="100%",
        align="center",
        gap="0",
    )


@template(
    route="/blog/[address]",
    title="Blog",
    on_load=BlogPostState.get_blog_post,
)
def blog_post() -> rx.Component:
    return rx.cond(
        BlogPostState.blog_post_is_loading,
        blog_post_loading(),
        rx.vstack(
            rx.image(
                src=BlogPostState.blog_post.image,
                width="100%",
                height="40vh",
                object_fit="cover",
            ),
            rx.vstack(
                rx.box(
                    button(
                        "Edit",
                        f"{routes.BLOG_ROUTE}/{BlogPostState.blog_post.address}/edit",
                        padding="20px",
                    ),
                    padding_top="1em",
                ),
                page_title(BlogPostState.blog_post.title, padding_bottom="5px"),
                align="center",
                width="100%",
                gap="0",
            ),
            rx.vstack(
                rx.text(
                    BlogPostState.get_str_datetime_for_post,
                ),
                rx.heading(
                    BlogPostState.blog_post.description,
                    size="5",
                    font_weight="300",
                ),
                rx.markdown(
                    BlogPostState.blog_post.content,
                    component_map=styles.markdown_style,
                ),
                width=styles.blog_post_content_width,
                align="center",
            ),
            width="100%",
            align="center",
            gap="0",
        ),
    )
