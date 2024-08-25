"""fy
from pathlib import Path
from typing import List


property fy_py_files_to_parse: List[Path]
"""

from pathlib import Path
from typing import List
import abc


# fy:start <<<===
class With_FyPyFilesToParse_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_files_to_parse(self) -> List[Path]:
        raise NotImplementedError()
        # fy:end <<<===
