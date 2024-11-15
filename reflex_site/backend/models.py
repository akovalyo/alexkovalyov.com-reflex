import reflex as rx
from datetime import datetime, timezone
import sqlalchemy
from sqlmodel import Field, Relationship, TEXT
from typing import Optional

# from sqlalchemy.dialects.postgresql import TEXT


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
    content: str = Field(sa_column=sqlalchemy.Column(TEXT))
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


class ContactMessage(rx.Model, table=True):
    email: str
    message: str = Field(sa_column=sqlalchemy.Column(TEXT))
    created_at: datetime = Field(
        default_factory=datetime.now(timezone.utc),
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False,
    )
