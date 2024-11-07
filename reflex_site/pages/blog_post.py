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
            rx.flex(
                # rx.spacer(),
                page_title(BlogPostState.blog_post.title, padding_bottom="5px"),
                # rx.spacer(),
                rx.box(
                    button(
                        "Edit",
                        f"{routes.BLOG_ROUTE}/{BlogPostState.blog_post.address}/edit",
                        padding="20px",
                    ),
                    padding_left="1em",
                    padding_top="1em",
                ),
                justify_self="flex-end",
                direction="row",
                wrap="wrap",
                justify="center",
                align="center",
                width="100%",
            ),
            rx.vstack(
                rx.heading(
                    BlogPostState.blog_post.description,
                    size="5",
                    font_weight="300",
                    # padding_bottom="0",
                ),
                rx.text(
                    BlogPostState.blog_post.content,
                    font_weight="300",
                    align="center",
                ),
                width=styles.blog_post_content_width,
                align="center",
            ),
            width="100%",
            align="center",
            gap="0",
        ),
    )
