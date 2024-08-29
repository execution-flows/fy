"""fy
method greet(greeting: str) -> int
"""

import abc


# fy:start ===>>>
class Greet_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _greet(self, greeting: str) -> int:
        raise NotImplementedError()
        # fy:end <<<===
