"""fy
flow HelloWorld -> None:
    method greet using constant
"""

from base.flow_base import FlowBase

from fy_py_files.test_fy_py_files.hello_world_using_method.using_constant_fy import (
    Greet_UsingConstant_MethodMixin,
)


# fy:start <<<===
class HelloWorld_Flow(
    # Method Mixins
    Greet_UsingConstant_MethodMixin,
    # Base
    FlowBase[None]
):
    def __call__(self) -> None:
        # fy:end <<<===
        self._greet()
