"""fy
from typing import List


property mixin_lines: List[str] using property_file_split:
    property property_file_split
"""

from mixins.property.property_file_split.abc_fy import (
    With_PropertyFileSplit_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start <<<===
class MixinLines_UsingPropertyFileSplit_PropertyMixin(
    # Property_mixins
    With_PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _mixin_lines(self) -> List[str]:
        # fy:end <<<===
        return self._property_file_split[5].split("\n")
