"""fy
from pathlib import Path


property folder_to_parse: Path
"""

from pathlib import Path
import abc


# fy:start ===>>>
class FolderToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _folder_to_parse(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
