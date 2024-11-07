import reflex as rx

border_radius = "var(--radius-2)"
border = f"2px solid {rx.color("accent", 3)}"
heading_color = rx.color("gray", 12)
text_color = rx.color("gray", 11)
accent_text_color = rx.color("accent", 10)
accent_bg_color = rx.color("accent", 3)
gray_bg_color = rx.color("gray", 3)
bar_color = rx.color("gray", 4)
sidebar_width = "32em"
sidebar_content_width = "16em"

base_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap",
    "styles.css",
]
base_style = {
    "font_family": "Oswald",
}

template_content_style = {
    "margin_bottom": "1em",
    "min_height": "85vh",
}

main_page_font_size = ["1em", "1.25em", "1.5em", "1.75em", "1.75em"]

card_project_width = ["70vw", "60vw", "200px", "220px", "260px"]
card_blog_width = ["70vw", "60vw", "240px", "260px", "300px"]
card_blog_height = ["42vw", "36vw", "120px", "132px", "156px"]

blog_post_content_width = ["80vw", "80vw", "80vw", "70vw", "60vw"]

form_max_width = ["75vw", "65vw", "55vw", "45vw", "35vw"]

markdown_style = {
    "h1": lambda text: rx.heading(text, size="7", margin_y="1em"),
    "h2": lambda text: rx.heading(text, size="6", margin_y="1em"),
    "h3": lambda text: rx.heading(text, size="5", margin_y="1em"),
    "h4": lambda text: rx.heading(text, size="4", margin_y="1em"),
    "h5": lambda text: rx.heading(text, size="3", margin_y="1em"),
    "h6": lambda text: rx.heading(text, size="2", margin_y="1em"),
    # "p": lambda text: rx.text(text, color="green", margin_y="1em"),
    "code": lambda text: rx.code(text, color_scheme="gray"),
    "codeblock": lambda text, **props: rx.code_block(text, **props, margin_y="1em"),
    "a": lambda text, **props: rx.link(
        text,
        **props,
        text_decoration="underline",
        text_decoration_color=accent_text_color,
    ),
}
