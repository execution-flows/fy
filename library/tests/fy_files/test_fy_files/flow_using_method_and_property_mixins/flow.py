from base.execution_flow_base import ExecutionFlowBase

from fy_files.test_fy_files.flow_using_method_and_property_mixins.greeting import (
    Greeting_UsingConstant_PropertyMixin,
)
from fy_files.test_fy_files.flow_using_method_and_property_mixins.greet import (
    Greet_UsingGreeting_MethodMixin,
)


class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Method Mixins
    Greet_UsingGreeting_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        self._greet()