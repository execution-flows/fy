"""fy
from typing import List


property abstract_property_file_split: List[str]
"""

from typing import List
import abc


# fy:start <<<===
class With_AbstractPropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_property_file_split(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
