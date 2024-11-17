import reflex as rx
import asyncio
from .. import styles
import copy


class MainState(rx.State):
    pending_callout: str = ""
    is_error: bool = True
    loading: bool = False

    async def check_callout(self):
        if self.pending_callout:

            if self.is_error:
                yield rx.toast.error(self.pending_callout)
            else:
                yield rx.toast.success(self.pending_callout)
            self.pending_callout = ""

    def set_pending_callout(
        self,
        message: str = "",
        is_error: bool = True,
    ):
        message = message if message else "Something went wrong."
        self.is_error = is_error
        self.pending_callout = message
