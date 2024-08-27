"""fy
from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile


property parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile
"""

from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile
import abc


# fy:start <<<===
class With_ParsedAbstractMethodFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_abstract_method_fy_py_file(self) -> ParsedAbstractMethodFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
