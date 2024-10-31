import reflex as rx


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("github", "https://github.com/akovalyo"),
        social_link("linkedin", "https://www.linkedin.com/in/alexandrkovalyov/"),
        social_link("instagram", "https://www.instagram.com/akovalyo/"),
        spacing="3",
        padding="1em",
        justify_content="center",
        width="100%",
    )
