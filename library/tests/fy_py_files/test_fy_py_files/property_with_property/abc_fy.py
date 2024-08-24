"""fy
property french_greeting: str
"""

import abc


# fy:start <<<===
class With_FrenchGreeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _french_greeting(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
