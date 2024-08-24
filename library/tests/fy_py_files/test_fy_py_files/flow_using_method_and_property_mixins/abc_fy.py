"""fy
property greeting: str
"""

import abc


# fy:start <<<===
class With_Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
