"""fy
from ..greetings_t import GreetingT


property greeting[GreetingT]
"""

import abc
from typing import Generic
from ..greetings_t import GreetingT


# fy:start ===>>>
class Greeting_PropertyMixin_ABC(
    Generic[GreetingT],
    abc.ABC,
):
    @property
    @abc.abstractmethod
    def _greeting(self) -> GreetingT:
        raise NotImplementedError()
        # fy:end <<<===
