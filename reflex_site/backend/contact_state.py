import reflex as rx
from .models import ContactMessage
from datetime import datetime, timezone
from ..backend import MainState
from ..navigation import routes


class ContactState(MainState):

    def handle_submit(self, form_data: dict):
        form_data["created_at"] = datetime.now(timezone.utc)
        with rx.session() as session:
            db_entry = ContactMessage(**form_data)
            session.add(db_entry)
            session.commit()
            self.set_pending_callout(
                "Your message has been submitted successfully.", False
            )
            return rx.redirect(routes.HOME_ROUTE)
