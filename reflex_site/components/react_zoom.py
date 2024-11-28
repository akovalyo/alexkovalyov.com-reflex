import reflex as rx


class ReactZoom(rx.Component):
    library = "react-medium-image-zoom"
    tag = "Zoom"

    is_default = True

    def add_imports(self):
        return {"": ["react-medium-image-zoom/dist/styles.css"]}


react_zoom = ReactZoom.create
