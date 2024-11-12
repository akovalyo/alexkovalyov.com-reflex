import reflex as rx

from ..templates import template
from ..navigation import routes
from ..backend import BlogPostState
from ..components import page_title, blog_card


@template(
    route=routes.BLOG_ROUTE,
    title="Blog",
    on_load=BlogPostState.load_blog_posts,
)
def blog() -> rx.Component:
    return rx.vstack(
        page_title("BLOG", padding_top="2em", padding_bottom="1em"),
        rx.flex(
            rx.foreach(BlogPostState.blog_posts, lambda item: blog_card(item)),
            direction="row",
            wrap="wrap",
            spacing="6",
            justify="center",
            align="center",
        ),
        width="100%",
        align="center",
    )
