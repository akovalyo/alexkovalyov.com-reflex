import reflex as rx


class ContactState(rx.State):

    def handle_submit(self, form_data: dict):
        print(form_data)
        pass
