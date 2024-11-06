import reflex as rx
from ..backend.models import BlogPost
from ..backend.state import BlogPostState


def blog_post_form_rows() -> rx.Component:
    return (
        rx.vstack(
            rx.input(
                name="title",
                placeholder="Title",
                default_value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.blog_post.title, ""
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.input(
                name="description",
                placeholder="Description",
                default_value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.blog_post.description, ""
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.input(
                name="image",
                placeholder="Image link",
                default_value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.blog_post.image, ""
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.text_area(
                name="content",
                placeholder="Content",
                value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.blog_post.content, ""
                ),
                on_change=BlogPostState.update_content_value,
                required=True,
                type="text",
                width="100%",
                height="30vh",
            ),
            rx.input(
                name="created_at",
                placeholder="Date",
                default_value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.get_str_datetime, ""
                ),
                required=False,
                type="datetime-local",
                width="100%",
            ),
            rx.input(
                name="address",
                placeholder="Address",
                default_value=rx.cond(
                    BlogPostState.blog_post, BlogPostState.blog_post.address, ""
                ),
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
    )
