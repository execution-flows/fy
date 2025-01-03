"""fy
method greet -> None using constant:
fy"""

import abc
from fy_py_files.test_fy_py_files.mixins.method.greet.abc_fy import (
    Greet_MethodMixin_ABC,
)


# fy:start ===>>>
class Greet_UsingConstant_MethodMixin(
    # Method Mixins
    Greet_MethodMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        # fy:end <<<===
        print("Hello World!")
