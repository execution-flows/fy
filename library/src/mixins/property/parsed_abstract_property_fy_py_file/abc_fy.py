"""fy
from domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile


property parsed_abstract_property_fy_py_file: ParsedAbstractPropertyFyPyFile
"""

from domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile
import abc


# fy:start ===>>>
class ParsedAbstractPropertyFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_abstract_property_fy_py_file(self) -> ParsedAbstractPropertyFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
