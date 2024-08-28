"""fy
from typing import List


property mixin_lines: List[str] using method_file_split:
    property method_file_split
"""

from mixins.property.method_file_split.abc_fy import (
    With_MethodFileSplit_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start <<<===
class MixinLines_UsingMethodFileSplit_PropertyMixin(
    # Property_mixins
    With_MethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _mixin_lines(self) -> List[str]:
        # fy:end <<<===
        return self._method_file_split[6].split("\n")
