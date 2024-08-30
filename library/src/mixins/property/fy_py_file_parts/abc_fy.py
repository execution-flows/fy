"""fy
from domain.parsed_fy_py_file import FyPyFileParts


property fy_py_file_parts: FyPyFileParts
"""

from domain.parsed_fy_py_file import FyPyFileParts
import abc


# fy:start ===>>>
class FyPyFileParts_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_py_file_parts(self) -> FyPyFileParts:
        raise NotImplementedError()
        # fy:end <<<===
