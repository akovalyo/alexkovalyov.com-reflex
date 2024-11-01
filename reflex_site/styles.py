import reflex as rx

border_radius = "var(--radius-2)"
border = f"1px solid {rx.color('gray', 5)}"
text_color = rx.color("gray", 11)
accent_text_color = rx.color("accent", 10)
accent_bg_color = rx.color("accent", 3)
gray_bg_color = rx.color("gray", 3)
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
