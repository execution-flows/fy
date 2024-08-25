"""fy
from typing import List
from domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files: List[ParsedFyPyFile]
"""

from domain.parsed_fy_py_file import ParsedFyPyFile
from typing import List
import abc


# fy:start <<<===
class With_ParsedFyPyFiles_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
