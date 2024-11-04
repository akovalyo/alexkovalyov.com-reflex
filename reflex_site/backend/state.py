import reflex as rx
from typing import List


class Project(rx.Base):
    type: str
    title: str
    description: str
    link: str
    link_title: str
    image: str
    link_secondary: str
    link_secondary_title: str


class Blog(rx.Base):
    type: str
    title: str
    description: str
    link: str
    image: str
    content: str
    date: str


class State(rx.State):
    projects: List[Project] = []
    blog: List[Blog] = []

    def load_projects(self):
        # load from db
        db_projects = [
            {
                "type": "blog",
                "title": "Flutter",
                "description": "Android app for an NFT project made in Flutter",
                "link": "https://github.com/akovalyo/wcdonalds_app",
                "link_title": "Code",
                "image": "/projects/flutter_app.jpg",
                "link_secondary": "",
                "link_secondary_title": "",
            },
            {
                "type": "project",
                "title": "CSS",
                "description": "CSS animation",
                "link": "https://codepen.io/akovalyo/full/WNporeY",
                "link_title": "Live",
                "image": "/projects/css_tree.png",
                "link_secondary": "",
                "link_secondary_title": "",
            },
            {
                "type": "project",
                "title": "React + Flask",
                "description": "Place to find local grown fruits and vegetables",
                "link": "https://github.com/akovalyo/instaHarvest",
                "link_title": "Code",
                "image": "/projects/instaharvest.png",
                "link_secondary": "",
                "link_secondary_title": "",
            },
            {
                "type": "project",
                "title": "Flutter Web",
                "description": "The website built in Flutter",
                "link": "https://github.com/akovalyo/alexkovalyov.com-flutter",
                "link_title": "Code",
                "image": "/projects/project_1.png",
                "link_secondary": "",
                "link_secondary_title": "",
            },
            {
                "type": "project",
                "title": "C",
                "description": "Recreating a real shell in C",
                "link": "https://github.com/akovalyo/42sv_minishell",
                "link_title": "Code",
                "image": "/projects/project_minishell.png",
                "link_secondary": "",
                "link_secondary_title": "",
            },
            {
                "type": "project",
                "title": "AI Project",
                "description": "Identifying white blood cells using CNN with Pytorch",
                "link": "https://github.com/akovalyo/wbc_classification",
                "link_title": "Code",
                "image": "/projects/blood.png",
                "link_secondary": "",
                "link_secondary_title": "",
            },
        ]

        self.projects = [Project(**item) for item in db_projects]
