"""fy
property greeting: str using greeting:
"""

from functools import cached_property


# fy:start ===>>>
class Greeting_UsingGreeting_PropertyMixin:
    @cached_property
    def _greeting(self) -> str:
        # fy:end <<<===
        return "Hello, World!"
