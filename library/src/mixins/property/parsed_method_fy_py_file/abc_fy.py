"""fy
from domain.parsed_fy_py_file import ParsedMethodFyPyFile


property parsed_method_fy_py_file: ParsedMethodFyPyFile
"""

from domain.parsed_fy_py_file import ParsedMethodFyPyFile
import abc


# fy:start ===>>>
class ParsedMethodFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_method_fy_py_file(self) -> ParsedMethodFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
