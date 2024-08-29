"""fy
method greet -> None using greeting:
    property greeting
"""

from fy_py_files.test_fy_py_files.flow_using_method_and_property_mixins.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
import abc


# fy:start ===>>>
class Greet_UsingGreeting_MethodMixin(
    # Property_mixins
    Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        # fy:end <<<===
        print(self._greeting)
