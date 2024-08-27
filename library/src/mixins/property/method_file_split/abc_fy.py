"""fy
from typing import List


property method_file_split: List[str]
"""

from typing import List
import abc


# fy:start <<<===
class With_MethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_file_split(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
