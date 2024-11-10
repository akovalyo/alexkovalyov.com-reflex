import reflex as rx
from ..backend.state import ProjectsState
from .. import styles


def project_form_rows() -> rx.Component:
    return (
        rx.vstack(
            rx.input(
                name="title",
                placeholder="Title",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.title,
                    "",
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.input(
                name="description",
                placeholder="Description",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.description,
                    "",
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.input(
                name="url",
                placeholder="Url",
                default_value=rx.cond(
                    ProjectsState.current_project, ProjectsState.current_project.url, ""
                ),
                required=False,
                type="text",
                width="100%",
            ),
            rx.input(
                name="url_title",
                placeholder="Url Title",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.url_title,
                    "",
                ),
                required=False,
                type="text",
                width="100%",
            ),
            rx.input(
                name="url_secondary",
                placeholder="Secondary Url",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.url_secondary,
                    "",
                ),
                required=False,
                type="text",
                width="100%",
            ),
            rx.input(
                name="url_secondary_title",
                placeholder="Secondary Url Title",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.url_secondary_title,
                    "",
                ),
                required=False,
                type="text",
                width="100%",
            ),
            rx.input(
                name="image",
                placeholder="Image link",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.current_project.image,
                    "",
                ),
                required=True,
                type="text",
                width="100%",
            ),
            rx.input(
                name="created_at",
                placeholder="Date",
                default_value=rx.cond(
                    ProjectsState.current_project,
                    ProjectsState.get_str_datetime_for_post,
                    "",
                ),
                required=False,
                type="datetime-local",
                width="100%",
            ),
            rx.button(
                "Submit",
                type="submit",
                cursor="pointer",
                background=styles.green_color,
            ),
            align="center",
        ),
    )
