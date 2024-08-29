"""fy
from domain.parsed_fy_py_file import ParsedPropertyFyPyFile


property parsed_property_fy_py_file: ParsedPropertyFyPyFile
"""

from domain.parsed_fy_py_file import ParsedPropertyFyPyFile
import abc


# fy:start ===>>>
class With_ParsedPropertyFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
