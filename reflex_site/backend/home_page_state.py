import reflex as rx
from .models import BlogPost, Project
from typing import List
from sqlmodel import select


class HomePageState(rx.State):
    latest_blog_posts: List["BlogPost"] = []
    latest_projects: List["Project"] = []

    def load_data_for_home_page(self):
        with rx.session() as session:
            projects = session.exec(
                select(Project).order_by(Project.created_at.desc()).limit(3)
            ).all()
            self.latest_projects = projects
            blog_posts = session.exec(
                select(BlogPost).order_by(BlogPost.created_at.desc()).limit(2)
            ).all()
            self.latest_blog_posts = blog_posts
