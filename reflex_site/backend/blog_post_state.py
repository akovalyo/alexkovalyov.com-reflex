import reflex as rx
from ..backend import BlogPost, BlogContent
from typing import List
from sqlmodel import select
from ..navigation import routes
from ..backend import proccess_form_data
from datetime import datetime, timezone

from ..backend import MainState
import asyncio
from .. import styles


class BlogPostState(MainState):
    blog_posts: List["BlogPost"] = []
    blog_post: BlogPost | None
    blog_post_content: str = ""
    blog_post_is_loading: bool = True

    @rx.var(cache=True)
    def _blog_post_address(self) -> str:
        return self.router.page.params.get("address", "")

    @rx.var(cache=True)
    def get_str_datetime_for_form(self) -> str:
        return (
            self.blog_post.created_at.strftime("%Y-%m-%dT%H:%m")
            if self.blog_post
            else ""
        )

    @rx.var(cache=True)
    def get_str_datetime_for_post(self) -> str:
        return self.blog_post.created_at.strftime("%Y-%m-%d") if self.blog_post else ""

    def get_empty_blog_post(self) -> BlogPost:
        content = BlogContent(content="")
        return BlogPost(
            id=None,
            title="",
            description="",
            image="",
            content=content,
            created_at=datetime.now(timezone.utc),
            address="",
        )

    def clear_current_blog_post(self):
        self.blog_post = self.get_empty_blog_post()
        self.blog_post_content = ""
        yield

    def update_content_value(self, value):
        self.blog_post.content.content = value

    def load_blog_posts(self):
        with rx.session() as session:
            res = session.exec(
                select(BlogPost).order_by(BlogPost.created_at.desc())
            ).all()
            self.blog_posts = res

    def get_blog_post(self):
        self.blog_post_is_loading = True
        with rx.session() as session:
            if self._blog_post_address == "":
                self.blog_post = None
                return rx.redirect(routes.PAGE_404_ROUTE)
            res = session.exec(
                select(BlogPost).where(BlogPost.address == self._blog_post_address)
            ).one_or_none()
            if not res:
                return rx.redirect(routes.PAGE_404_ROUTE)
            self.blog_post = res
            self.blog_post_content = res.content.content
            self.blog_post_is_loading = False

    def add_blog_post(self, form_data: dict):
        content = form_data["content"]
        data = proccess_form_data(form_data)

        with rx.session() as session:
            db_blogpost = BlogPost(**data)
            db_content = BlogContent(content=content)
            db_blogpost.content = db_content
            session.add(db_blogpost)
            session.commit()
            self.set_pending_callout("Blog post added.", False)
            self.clear_current_blog_post()

        return rx.redirect(routes.BLOG_ROUTE)

    def edit_blog_post(self, form_data: dict):
        content = form_data["content"]
        data = proccess_form_data(form_data)
        with rx.session() as session:
            res = session.get(BlogPost, self.blog_post.id)
            if res:
                for k, v in data.items():
                    setattr(res, k, v)
                res.content.content = content
                session.add(res)
                session.commit()
                self.set_pending_callout("Blog post updated.", False)
            else:
                return rx.redirect("/404")

            return rx.redirect(f"{routes.BLOG_ROUTE}/{self.blog_post.address}")

    def delete_blog_post(self):
        with rx.session() as session:
            res = session.get(BlogPost, self.blog_post.id)
            if res:
                session.delete(res.content)
                session.delete(res)
                session.commit()
                self.set_pending_callout("Blog post deleted.", False)
            else:
                self.set_pending_callout(
                    "Failed to delete the blogpost. Try again later."
                )
            self.clear_current_blog_post()
            return rx.redirect(routes.BLOG_ROUTE)
