import reflex as rx
from .. import styles
from ..navigation import routes
from datetime import datetime
import reflex_local_auth as rxa


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.icon(icon),
        href=href,
        is_external=True,
    )


def social_tab() -> rx.Component:
    return rx.flex(
        social_link("github", "https://github.com/akovalyo"),
        social_link("linkedin", "https://www.linkedin.com/in/alexandrkovalyov/"),
        social_link("instagram", "https://www.instagram.com/akovalyo/"),
        spacing="3",
        padding="1em",
        justify_content="center",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.vstack(
        social_tab(),
        rx.hstack(
            rx.text(
                "Built with",
                size="2",
                weight="light",
            ),
            rx.link(
                rx.image(
                    src="/reflex_logo.jpg",
                    width="1em",
                    height="auto",
                    border_radius="25%",
                ),
                href="https://reflex.dev",
            ),
            justify_content="center",
            width="100%",
        ),
        rx.text(
            f"Copyright Alex Kovalyov © {datetime.now().year}",
            white_space="nowrap",
            weight="light",
            size="2",
        ),
        width="100%",
        justify_content="center",
        spacing="0",
        align="center",
    )


def menu_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=20)


def logout_menu_item() -> rx.Component:
    return rx.link(
        rx.hstack(
            menu_item_icon("log-out"),
            rx.text("Log Out", size="4", weight="regular"),
            color=styles.text_color,
            style={
                "_hover": {
                    "background_color": styles.gray_bg_color,
                    "color": styles.text_color,
                    "opacity": "1",
                },
                "opacity": "0.95",
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.35em",
        ),
        underline="none",
        href=routes.HOME_ROUTE,
        on_click=rxa.LocalAuthState.do_logout,
        width="100%",
    )


def menu_item(text: str, url: str, active: bool = True) -> rx.Component:
    if active:
        active = rx.State.router.page.path == url.lower()
    else:
        active = False

    return rx.link(
        rx.hstack(
            rx.match(
                text,
                ("Home", menu_item_icon("home")),
                ("Projects", menu_item_icon("folder-kanban")),
                ("Blog", menu_item_icon("notebook-text")),
                ("Add Blog", menu_item_icon("list-plus")),
                ("Add Project", menu_item_icon("folder-plus")),
                ("Log In", menu_item_icon("log-in")),
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


def menu_items() -> rx.Component:
    public_items = [
        {
            "title": "Home",
            "path": routes.HOME_ROUTE,
        },
        {
            "title": "Projects",
            "path": routes.PROJECTS_ROUTE,
        },
        {
            "title": "Blog",
            "path": routes.BLOG_ROUTE,
        },
    ]

    auth_items = [
        {
            "title": "Add Project",
            "path": routes.ADD_PROJECT_ROUT,
        },
        {
            "title": "Add Blog",
            "path": routes.ADD_BLOG_POST_ROUT,
        },
    ]

    return rx.vstack(
        *[
            menu_item(
                text=item["title"],
                url=item["path"],
            )
            for item in public_items
        ],
        rx.divider(),
        rx.cond(
            rxa.LocalAuthState.is_authenticated,
            rx.vstack(
                *[
                    menu_item(
                        text=item["title"],
                        url=item["path"],
                    )
                    for item in auth_items
                ],
                logout_menu_item(),
            ),
            menu_item(text="Log In", url=routes.LOGIN_ROUTE, active=False),
        ),
        width="100%",
    )


def navbar_menu_button() -> rx.Component:
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
                    menu_items(),
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


def logo() -> rx.Component:
    return rx.link(
        rx.color_mode_cond(
            rx.image(src="/ak_gray.svg", height="2em"),
            rx.image(src="/ak_white.svg", height="2em"),
        ),
        on_click=lambda: rx.redirect(routes.HOME_ROUTE),
        cursor="pointer",
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.hstack(
            logo(),
            rx.spacer(),
            rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
            navbar_menu_button(),
            align="center",
            width="100%",
            padding_y="1em",
            padding_x=["1em", "1em", "2em"],
        ),
        display=["block", "block", "block", "block", "block", "none"],
        position="sticky",
        background_color=styles.bar_color,
        top="0px",
        z_index="5",
    )


def sidebar() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
                rx.spacer(),
                logo(),
                align="center",
                width="100%",
                padding="0.35em",
                margin_bottom="1em",
            ),
            rx.flex(
                menu_items(),
                justify="end",
            ),
            rx.spacer(),
            footer(),
            justify="end",
            align="end",
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="1em",
        ),
        display=["none", "none", "none", "none", "none", "flex"],
        max_width=styles.sidebar_width,
        width="auto",
        height="100%",
        position="sticky",
        justify="end",
        top="0px",
        left="0px",
        flex="1",
        bg=styles.bar_color,
    )
