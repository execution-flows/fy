"""fy
from typing import List


property mixin_lines: List[str]
"""

import abc
from typing import List


# fy:start ===>>>
class With_MixinLines_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_lines(self) -> List[str]:
        raise NotImplementedError()
        # fy:end <<<===
