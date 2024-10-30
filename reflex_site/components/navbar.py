import reflex as rx
from .. import styles
from reflex.page import get_decorated_pages
from ..components.footer import footer


def menu_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=20)


def menu_item(text: str, url: str) -> rx.Component:
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & text == "Home"
    )

    return rx.link(
        rx.hstack(
            rx.match(
                text,
                ("Home", menu_item_icon("home")),
            ),
            rx.text(text, size="4", weight="regular"),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            style={
                "_hover": {
                    "background_color": rx.cond(
                        active,
                        styles.accent_bg_color,
                        styles.gray_bg_color,
                    ),
                    "color": rx.cond(
                        active,
                        styles.accent_text_color,
                        styles.text_color,
                    ),
                    "opacity": "1",
                },
                "opacity": rx.cond(
                    active,
                    "1",
                    "0.95",
                ),
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.35em",
        ),
        underline="none",
        href=url,
        width="100%",
    )


def menu_button() -> rx.Component:
    ordered_page_routes = [
        "/",
    ]
    pages = get_decorated_pages()
    ordered_pages = sorted(
        pages,
        key=lambda page: (
            ordered_page_routes.index(page["route"])
            if page["route"] in ordered_page_routes
            else len(ordered_page_routes)
        ),
    )

    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon(
                "align-justify",
                cursor="pointer",
            ),
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.hstack(
                        rx.spacer(),
                        rx.drawer.close(
                            rx.icon(
                                tag="x",
                                cursor="pointer",
                            )
                        ),
                        justify="end",
                        width="100%",
                    ),
                    rx.divider(),
                    *[
                        menu_item(
                            text=page.get(
                                "title", page["route"].strip("/").capitalize()
                            ),
                            url=page["route"],
                        )
                        for page in ordered_pages
                    ],
                    rx.spacer(),
                    footer(),
                    spacing="4",
                    width="100%",
                ),
                top="auto",
                left="auto",
                height="100%",
                width="20em",
                padding="1em",
                bg=rx.color("gray", 1),
            ),
            width="100%",
        ),
        direction="right",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.hstack(
            rx.link(
                rx.color_mode_cond(
                    rx.image(src="/ak_gray.svg", height="2em"),
                    rx.image(src="/ak_white.svg", height="2em"),
                ),
                on_click=rx.redirect("/"),
                cursor="pointer",
            ),
            rx.spacer(),
            rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
            menu_button(),
            align="center",
            width="100%",
            padding_y="1em",
            padding_x=["1em", "1em", "2em"],
        ),
        display=["block", "block", "block", "block", "block", "none"],
        position="sticky",
        background_color=rx.color("gray", 1),
        top="0px",
        z_index="5",
        border_bottom=styles.border,
    )
