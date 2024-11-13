import reflex as rx
from .models import ContactMessage
from datetime import datetime, timezone
from ..backend import MainState, get_error_message
from ..navigation import routes


class ContactState(MainState):

    def handle_submit(self, form_data: dict):
        form_data["created_at"] = datetime.now(timezone.utc)
        self.loading = True
        yield
        try:
            with rx.session() as session:
                db_entry = ContactMessage(**form_data)
                session.add(db_entry)
                session.commit()
                self.set_pending_callout(
                    "Your message has been submitted successfully.", False
                )

        except Exception as e:
            print(get_error_message(e))
            self.set_pending_callout()
        self.loading = False
        yield
        return rx.redirect(routes.HOME_ROUTE)
