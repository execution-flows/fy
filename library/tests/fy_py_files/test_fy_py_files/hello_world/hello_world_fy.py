"""fy
flow HelloWorld -> None:
"""

from fy_core.base.flow_base import FlowBase


# fy:start ===>>>
class HelloWorld_Flow(
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
