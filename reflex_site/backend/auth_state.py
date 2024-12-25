import reflex as rx
import reflex_local_auth as rxa
from ..navigation import routes
from ..backend import MainState
import os


class AuthState(rxa.RegistrationState):

    def handle_registration(
        self, form_data
    ) -> rx.event.EventSpec | list[rx.event.EventSpec]:  # type: ignore
        """Handle registration form on_submit.

        Set error_message appropriately based on validation results.

        Args:
            form_data: A dict of form fields and values.
        """
        username = form_data["username"]
        password = form_data["password"]
        code = form_data["code"]
        validation_errors = self._validate_fields(
            username, password, form_data["confirm_password"]
        )
        print(validation_errors)
        # if code != os.getenv("REGISTRATION_CODE"):
        #     validation_errors = ["Invalid registration code"]
        if validation_errors or code != os.getenv("REGISTRATION_CODE"):
            self.new_user_id = -1
            return validation_errors
        self._register_user(username, password)
        return type(self).successful_registration
