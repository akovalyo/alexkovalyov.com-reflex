import reflex as rx
from typing import Callable
from ..components import navbar, sidebar
from .. import styles
from ..backend import ThemeState
from ..backend import MainState

default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]


def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,  # type: ignore
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return (
                rx.flex(
                    navbar(),
                    sidebar(),
                    rx.flex(
                        rx.vstack(
                            page_content(),
                            width="100%",
                            **styles.template_content_style,
                            align="center",
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
            )

        on_load_list = (
            on_load
            if isinstance(on_load, list)
            else [on_load] if isinstance(on_load, rx.event.EventHandler) else []
        ) + [MainState.check_callout]

        @rx.page(
            route=route,
            title=title,
            description=description,
            meta=all_meta,
            on_load=on_load_list,
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
