import abc

from fy_files.test_fy_files.flow_using_method_and_property_mixins.abc import (
    With_Greeting_PropertyMixin_ABC,
)


class Greet_UsingGreeting_MethodMixin(
    # Property_mixins
    With_Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        print(self._greeting)