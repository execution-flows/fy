"""fy
flow HelloWorld -> None:
    method greet using constant
"""

from base.execution_flow_base import ExecutionFlowBase

from fy_py_files.test_fypy_files.hello_world_using_method.using_constant_fy import (
    Greet_UsingConstant_MethodMixin,
)


# fy:start <<<===
class Helloworld_Flow(
    # Method Mixins
    Greet_UsingConstant_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        self._greet()
