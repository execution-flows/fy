"""fy
import datetime


property greeting: datetime.datetime
"""

import abc
import datetime


# fy:start ===>>>
class Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> datetime.datetime:
        raise NotImplementedError()
        # fy:end <<<===
