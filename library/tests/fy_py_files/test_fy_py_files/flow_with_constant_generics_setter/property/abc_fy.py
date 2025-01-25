"""fy
from .greetings_t import GreetingT

property greeting[GreetingT]: str
fy"""

import abc
from typing import Generic
from .greetings_t import GreetingT


# fy:start ===>>>
class Greeting_PropertyMixin_ABC(
    Generic[GreetingT],
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
