"""fy
flow HelloWorld -> None:
    property greeting using constant
"""

from base.flow_base import FlowBase

from fy_py_files.test_fy_py_files.hello_world_using_property.property.using_constant_fy import (
    Greeting_UsingConstant_PropertyMixin,
)


# fy:start ===>>>
class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        print(self._greeting)
