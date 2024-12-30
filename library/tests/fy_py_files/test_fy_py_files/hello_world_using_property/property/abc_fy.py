"""fy
from pathlib import Path

property greeting: Path
fy"""

import abc
from pathlib import Path


# fy:start ===>>>
class Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
