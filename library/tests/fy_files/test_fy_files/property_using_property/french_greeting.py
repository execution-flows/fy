from functools import cached_property

import abc

from fy_files.test_fy_files.property_using_property.abc import (
    With_FrenchGreeting_PropertyMixin_ABC,
)


class Greeting_UsingFrenchGreeting_PropertyMixin(
    # Property_mixins
    With_FrenchGreeting_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> str:
        return self._french_greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
