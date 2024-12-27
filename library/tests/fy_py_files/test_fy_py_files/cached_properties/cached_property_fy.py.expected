"""fy
property greeting: str using greeting:
"""

from functools import cached_property
import abc
from fy_py_files.test_fy_py_files.cached_properties.abc_fy import (
    Greeting_PropertyMixin_ABC,
)


# fy:start ===>>>
class Greeting_UsingGreeting_PropertyMixin(
    # Property_mixins
    Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _greeting(self) -> str:
        # fy:end <<<===
        return "Hello, World!"
