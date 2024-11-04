import reflex as rx
from typing import List
from datetime import datetime


class Project(rx.Base):
    category: str
    title: str
    description: str
    link: str
    link_title: str
    image: str
    link_secondary: str
    link_secondary_title: str
    date: str


class Blog(rx.Base):
    category: str
    title: str
    description: str
    link: str
    image: str
    content: str
    date: str
    date_f: str = ""


class State(rx.State):
    projects: List[Project] = []
    blog: List[Blog] = []

    def load_projects(self):
        # load from db
        db_projects = [
            {
                "category": "project",
                "title": "Flutter",
                "description": "Android app for an NFT project made in Flutter",
                "link": "https://github.com/akovalyo/wcdonalds_app",
                "link_title": "Code",
                "image": "/projects/flutter_app.jpg",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
            {
                "category": "project",
                "title": "CSS",
                "description": "CSS animation",
                "link": "https://codepen.io/akovalyo/full/WNporeY",
                "link_title": "Live",
                "image": "/projects/css_tree.png",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
            {
                "category": "project",
                "title": "React + Flask",
                "description": "Place to find local grown fruits and vegetables",
                "link": "https://github.com/akovalyo/instaHarvest",
                "link_title": "Code",
                "image": "/projects/instaharvest.png",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
            {
                "category": "project",
                "title": "Flutter Web",
                "description": "The website built in Flutter",
                "link": "https://github.com/akovalyo/alexkovalyov.com-flutter",
                "link_title": "Code",
                "image": "/projects/project_1.png",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
            {
                "category": "project",
                "title": "C",
                "description": "Recreating a real shell in C",
                "link": "https://github.com/akovalyo/42sv_minishell",
                "link_title": "Code",
                "image": "/projects/project_minishell.png",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
            {
                "category": "project",
                "title": "AI Project",
                "description": "Identifying white blood cells using CNN with Pytorch",
                "link": "https://github.com/akovalyo/wbc_classification",
                "link_title": "Code",
                "image": "/projects/blood.png",
                "link_secondary": "",
                "link_secondary_title": "",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
        ]

        self.projects = [Project(**item) for item in db_projects]

    def load_blog(self):
        # load from db
        db_blog = [
            {
                "category": "blog",
                "title": "Python and Env Cheat Sheet",
                "description": "Managing python environments",
                "link": "https://github.com/akovalyo/wcdonalds_app",
                "image": "/python.png",
                "content": "text",
                "date": "2024-11-04T20:30:22.352057+00:00",
            },
        ]

        self.blog = [Blog(**item) for item in db_blog]
        for item in self.blog:
            item.date_f = datetime.fromisoformat(item.date).strftime("%Y-%m-%d")
