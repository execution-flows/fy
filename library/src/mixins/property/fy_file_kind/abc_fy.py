"""fy
from domain.parsed_fy_py_file import ParsedFyPyFileKind


property fy_file_kind: ParsedFyPyFileKind
"""

from domain.parsed_fy_py_file import ParsedFyPyFileKind
import abc


# fy:start ===>>>
class FyFileKind_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        raise NotImplementedError()
        # fy:end <<<===
