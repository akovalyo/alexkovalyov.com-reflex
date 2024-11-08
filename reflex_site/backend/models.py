import reflex as rx
from datetime import datetime, timezone
import sqlalchemy
from sqlmodel import Field, Relationship
from typing import Optional


class BlogPost(rx.Model, table=True):
    title: str
    description: str
    image: str
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
    address: str
    content: "BlogContent" = Relationship()


class BlogContent(rx.Model, table=True):
    content: str
    blogpost_id: int = Field(foreign_key="blogpost.id")


class Project(rx.Model, table=True):
    title: str
    description: str
    url: str | None = None
    url_title: str | None = None
    url_secondary: str | None = None
    url_secondary_title: str | None = None
    image: str
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
