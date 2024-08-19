from fy_files.test_fy_files.hello_world_using_property.property.using_constant import (
    Greeting_UsingConstant_PropertyMixin,
)

from base.execution_flow_base import ExecutionFlowBase


class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        print(self._greeting)
