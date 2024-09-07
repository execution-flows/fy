"""fy
property greeting: str using french_greeting:
    property french_greeting
"""

from functools import cached_property
import abc
from fy_py_files.test_fy_py_files.property_with_property.abc_fy import (
    FrenchGreeting_PropertyMixin_ABC,
)


# fy:start ===>>>
class Greeting_UsingFrenchGreeting_PropertyMixin(
    # Property_mixins
    FrenchGreeting_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> str:
        # fy:end <<<===
        return self._french_greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
