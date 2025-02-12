"""fy
from fy_py_files.test_fy_py_files.method_implementing_own_generics.greetings_t import SpanishGreeting

flow hello_world2 -> str:
    property greeting using setter[SpanishGreeting]
fy"""

from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.flow_with_constant_generics_setter.property.using_setter import (
    Greeting_UsingSetter_PropertyMixin,
)
from typing import Any
from fy_py_files.test_fy_py_files.method_implementing_own_generics.greetings_t import (
    SpanishGreeting,
)


# fy:start ===>>>
class HelloWorld2_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin[SpanishGreeting],
    # Base
    FlowBase[str],
):
    def __init__(
        self,
        *args: Any,
        greeting: SpanishGreeting,
        **kwargs: Any,
    ):
        self._greeting = greeting
        super().__init__(*args, **kwargs)

    def __call__(self) -> str:
        # fy:end <<<===
        return self._greeting
