import reflex as rx
from datetime import datetime, timezone
import sqlalchemy
from sqlmodel import Field


class BlogPost(rx.Model, table=True):
    category: str
    title: str
    description: str
    image: str
    content: str
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
    address: str


class Project(rx.Model, table=True):
    category: str
    title: str
    description: str
    link: str
    link_title: str
    link_secondary: str
    link_secondary_title: str
    image: str
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
