"""fy
method greet(argument: str) -> None using greeting:
    property greeting
"""

import abc

from fy_py_files.test_fy_py_files.mixins.method.with_property.abc_fy import (
    With_Greeting_PropertyMixin_ABC,
)


# fy:start <<<===
class Greet_UsingGreeting_MethodMixin(
    # Property_mixins
    With_Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    def _greet(self, argument: str) -> None:
        # fy:end <<<===
        print(self._greeting + argument)
