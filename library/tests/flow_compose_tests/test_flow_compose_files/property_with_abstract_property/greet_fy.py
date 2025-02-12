"""fy
property greet: int using constant:
    property greeting
fy"""

from functools import cached_property


# fy:start ===>>>
class Greet_UsingEncrypt_PropertyMixin:
    @cached_property
    def _greet(self) -> int:
        # fy:end <<<===
        print(self._greeting)
        print(self._greeting)
        return 1
