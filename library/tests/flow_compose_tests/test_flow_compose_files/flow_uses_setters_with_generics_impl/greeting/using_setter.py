# fy:start ===>>>
from typing import Generic
from ..greetings_t import GreetingT


class Greeting_UsingSetter_PropertyMixin(Generic[GreetingT]):
    @property
    def _greeting(self) -> GreetingT:
        return self.__greeting

    @_greeting.setter
    def _greeting(self, greeting: GreetingT) -> None:
        self.__greeting = greeting


# fy:end <<<===
