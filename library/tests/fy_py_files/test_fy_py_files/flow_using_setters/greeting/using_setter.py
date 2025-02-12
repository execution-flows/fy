# fy:start ===>>>
import datetime


class Greeting_UsingSetter_PropertyMixin:
    @property
    def _greeting(self) -> datetime.datetime:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: datetime.datetime) -> None:
        self.__greeting = greeting


# fy:end <<<===
