"""fy
from pathlib import Path


property project_root_folder: Path
"""

import abc
from pathlib import Path


# fy:start ===>>>
class ProjectRootFolder_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _project_root_folder(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
