import reflex as rx
from typing import Callable

from ..components.footer import footer
from .. import styles

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


class ThemeState(rx.State):
    accent_color: str = "tomato"
    gray_color: str = "gray"
    radius: str = "large"
    scaling: str = "100%"


def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.flex(
                rx.flex(
                    rx.flex(
                        rx.vstack(
                            page_content(),
                            width="100%",
                            **styles.template_content_style,
                        ),
                        width="100%",
                    ),
                    flex_direction=[
                        "column",
                        "column",
                        "column",
                        "column",
                        "column",
                        "row",
                    ],
                    width="100%",
                    margin="auto",
                    position="relative",
                ),
                footer(),
                flex_direction="column",
            )

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color,
                radius=ThemeState.radius,
                scaling=ThemeState.scaling,
            )

        return theme_wrap

    return decorator
