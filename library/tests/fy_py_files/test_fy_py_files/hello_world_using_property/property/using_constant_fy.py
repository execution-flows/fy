"""fy
from pathlib import Path

property greeting: Path using constant:
"""

from pathlib import Path


# fy:start <<<===
class Greeting_UsingConstant_PropertyMixin:
    @property
    def _greeting(self) -> Path:
        # fy:end <<<===
        return Path("")
