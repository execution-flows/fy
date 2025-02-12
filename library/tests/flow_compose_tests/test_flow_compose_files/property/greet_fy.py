"""fy
property greet: int using constant:
fy"""

from functools import cached_property


# fy:start ===>>>
class Greet_UsingEncrypt_PropertyMixin:
    @cached_property
    def _greet(self) -> int:
        # fy:end <<<===
        return 1
