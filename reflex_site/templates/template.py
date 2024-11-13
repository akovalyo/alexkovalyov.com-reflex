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
                            rx.cond(
                                MainState.callout,
                                rx.flex(
                                    rx.box(
                                        rx.hstack(
                                            rx.icon(
                                                "info",
                                                size=20,
                                                margin_right="5px",
                                            ),
                                            MainState.callout.message,
                                            width="100%",
                                            align="center",
                                            justify="center",
                                            gap="0",
                                            padding="0.75em 0",
                                        ),
                                        border_radius=styles.border_radius,
                                        width="100%",
                                        background_color=MainState.callout.color,
                                        style={
                                            "opacity": "0.8",
                                            "color": "white",
                                            "animation": "reveal 0.3s ease both",
                                            "@keyframes reveal": {
                                                "0%": {
                                                    "opacity": "0",
                                                    "transform": "scale(0)",
                                                },
                                                "100%": {
                                                    "opacity": "0.8",
                                                    "transform": "scale(1)",
                                                },
                                            },
                                        },
                                    ),
                                    align="center",
                                    justify="center",
                                    width="50vw",
                                    style={
                                        "position": "fixed",
                                        "bottom": "2em",
                                        "z_index": "6",
                                    },
                                ),
                            ),
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
