"""fy
from domain.parsed_fy_py_file import ParsedFlowFyPyFile


property parsed_flow_fy_py_file: ParsedFlowFyPyFile
"""

from domain.parsed_fy_py_file import ParsedFlowFyPyFile
import abc


# fy:start ===>>>
class ParsedFlowFyPyFile_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_flow_fy_py_file(self) -> ParsedFlowFyPyFile:
        raise NotImplementedError()
        # fy:end <<<===
