"""fy
flow hello_world2 -> str:
    property greeting using setter
fy"""

from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.flow_with_constant_setter.property.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)
from typing import Any


# fy:start ===>>>
class HelloWorld2_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin,
    # Base
    FlowBase[str],
):
    def __init__(
        self,
        *args: Any,
        greeting: str,
        **kwargs: Any,
    ):
        self._greeting = greeting
        super().__init__(*args, **kwargs)

    def __call__(self) -> str:
        # fy:end <<<===
        print(self._greeting)
