import abc

from fy_files.test_fy_files.mixins.method.using_property.abc import (
    With_Greeting_PropertyMixin_ABC,
)


class Greet_UsingGreeting_MethodMixin(
    # Property_mixins
    With_Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    def _greet(self, argument: str) -> None:
        print(self._greeting)
