"""fy
property greeting: str using french_greeting:
    property french_greeting
"""

import abc

from fy_py_files.test_fy_py_files.property_with_property.abc_fy import (
    With_FrenchGreeting_PropertyMixin_ABC,
)


from functools import cached_property


# fy:start <<<===
class Greeting_UsingFrenchGreeting_PropertyMixin(
    # Property_mixins
    With_FrenchGreeting_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> str:
        # fy:end <<<===
        return self._french_greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
