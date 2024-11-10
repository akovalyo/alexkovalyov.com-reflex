import reflex as rx
from .models import ContactMessage
from datetime import datetime, timezone


class ContactState(rx.State):

    def handle_submit(self, form_data: dict):
        form_data["created_at"] = datetime.now(timezone.utc)
        with rx.session() as session:
            db_entry = ContactMessage(**form_data)
            session.add(db_entry)
            session.commit()

        # TODO send confirmation message
