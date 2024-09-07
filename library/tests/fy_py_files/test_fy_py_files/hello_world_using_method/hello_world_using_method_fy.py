"""fy
base flow HelloWorld -> None:
    method greet using constant
"""

import abc
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.hello_world_using_method.using_constant_fy import (
    Greet_UsingConstant_MethodMixin,
)


# fy:start ===>>>
class HelloWorld_BaseFlow(
    # Method Mixins
    Greet_UsingConstant_MethodMixin,
    # Base
    FlowBase[None],
    abc.ABC,
):
    pass
    # fy:end <<<===
