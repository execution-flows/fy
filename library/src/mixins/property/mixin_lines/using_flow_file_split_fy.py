"""fy
from typing import List


property mixin_lines: List[str] using flow_file_split:
    property flow_file_split
"""

from functools import cached_property
from mixins.property.flow_file_split.abc_fy import (
    With_FlowFileSplit_PropertyMixin_ABC,
)
from typing import List
import abc


# fy:start ===>>>
class MixinLines_UsingFlowFileSplit_PropertyMixin(
    # Property_mixins
    With_FlowFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_lines(self) -> List[str]:
        # fy:end <<<===
        return self._flow_file_split.mixin_split.split("\n")
