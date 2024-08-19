from base.execution_flow_base import ExecutionFlowBase

from fy_files.test_fy_files.hello_world_using_method.using_constant import (
    Greet_UsingConstant_MethodMixin,
)


class HelloWorld_Flow(
    # Method Mixins
    Greet_UsingConstant_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        self._greet()
