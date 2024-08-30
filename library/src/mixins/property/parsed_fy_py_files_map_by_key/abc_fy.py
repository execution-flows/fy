"""fy
from typing import Dict
from domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile]
"""

from domain.parsed_fy_py_file import ParsedFyPyFile
from typing import Dict
import abc


# fy:start ===>>>
class ParsedFyPyFilesMapByKey_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
