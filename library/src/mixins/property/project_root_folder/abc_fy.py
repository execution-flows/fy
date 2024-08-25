"""fy
from pathlib import Path


property project_root_folder: Path
"""

from pathlib import Path
import abc


# fy:start <<<===
class With_ProjectRootFolder_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _project_root_folder(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
