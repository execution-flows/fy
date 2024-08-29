"""fy
from typing import List


property abstract_method_file_split: List[str]
"""

from typing import List
import abc


# fy:start ===>>>
class With_AbstractMethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_method_file_split(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
