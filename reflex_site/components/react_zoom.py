import reflex as rx


class ReactZoom(rx.Component):
    library = "react-medium-image-zoom"
    tag = "Zoom"
    is_default = True


react_zoom = ReactZoom.create
