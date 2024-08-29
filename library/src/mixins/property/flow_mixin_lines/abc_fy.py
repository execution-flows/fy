"""fy
from typing import List


property flow_mixin_lines: List[str]
"""

from typing import List
import abc


# fy:start ===>>>
class With_FlowMixinLines_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _flow_mixin_lines(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
