"""fy
from pathlib import Path


property fy_py_file_to_parse: Path
"""

from pathlib import Path
import abc


# fy:start ===>>>
class FyPyFileToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_file_to_parse(self) -> Path:
        raise NotImplementedError()
        # fy:end <<<===
