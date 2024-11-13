import reflex as rx
import asyncio
from .. import styles
import copy


class Callout(rx.Base):
    message: str
    color: str
    timeout: int


class MainState(rx.State):
    callout: Callout | None
    pending_callout: Callout | None
    running: bool = False
    loading: bool = False

    async def check_callout(self):
        if self.pending_callout and not self.running:
            self.running = True
            self.callout = copy.deepcopy(self.pending_callout)
            self.pending_callout = None
            yield
            await asyncio.sleep(self.callout.timeout)
            self.callout = None
            yield
            self.running = False

    def set_pending_callout(
        self, message: str = "", is_alert: bool = True, timeout: int = 5
    ):
        message = message if message else "Something went wrong."
        color = styles.callout_alert if is_alert else styles.callout_green
        self.pending_callout = Callout(message=message, color=color, timeout=timeout)

    async def async_callout(
        self, message: str = "", is_alert: bool = True, timeout: int = 5
    ):
        message = message if message else "Something went wrong."
        color = styles.callout_alert if is_alert else styles.callout_green
        self.callout = Callout(message=message, color=color, timeout=timeout)
        self.running = True
        yield
        await asyncio.sleep(self.callout.timeout)
        self.callout = None
        yield
        self.running = False
