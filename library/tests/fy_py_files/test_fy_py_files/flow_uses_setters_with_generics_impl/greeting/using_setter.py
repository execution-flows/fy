# fy:start ===>>>
from typing import Generic
from fy_py_files.test_fy_py_files.flow_uses_setters_with_generics_impl.greeting.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from ..greetings_t import GreetingT


class Greeting_UsingSetter_PropertyMixin(
    Greeting_PropertyMixin_ABC, Generic[GreetingT]
):
    @property
    def _greeting(self) -> GreetingT:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: GreetingT) -> None:
        self.__greeting = greeting


# fy:end <<<===
