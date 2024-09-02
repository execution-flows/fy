"""fy
flow HelloWorld -> None:
    property greeting using constant
    method greet using greeting
"""

from fy_core import FlowBase
from fy_py_files.test_fy_py_files.flow_using_method_and_property_mixins.greet_fy import (
    Greet_UsingGreeting_MethodMixin,
)
from fy_py_files.test_fy_py_files.flow_using_method_and_property_mixins.greeting_fy import (
    Greeting_UsingConstant_PropertyMixin,
)


# fy:start ===>>>
class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Method Mixins
    Greet_UsingGreeting_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        self._greet()
