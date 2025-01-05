# fy:start ===>>>
from fy_py_files.test_fy_py_files.flow_using_setters.greeting.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
import datetime


class Greeting_UsingSetter_PropertyMixin(
    Greeting_PropertyMixin_ABC,
):
    @property
    def _greeting(self) -> datetime.datetime:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: datetime.datetime) -> None:
        self.__greeting = greeting


# fy:end <<<===
