"""fy
property greeting2: str
fy"""

import abc


# fy:start ===>>>
class Greeting2_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting2(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
