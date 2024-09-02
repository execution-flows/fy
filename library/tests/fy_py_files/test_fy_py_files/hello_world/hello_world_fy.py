"""fy
flow HelloWorld -> None:
"""

from fy_core import FlowBase


# fy:start ===>>>
class HelloWorld_Flow(
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
