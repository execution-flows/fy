"""fy
from typing import List
from domain.parsed_fy_py_file import ParsedFyPyFile

property required_property_setters_fy_py: List[ParsedFyPyFile]
"""

from domain.parsed_fy_py_file import ParsedFyPyFile
from typing import List
import abc


# fy:start ===>>>
class With_RequiredPropertySettersFyPy_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        raise NotImplementedError()
        # fy:end <<<===
