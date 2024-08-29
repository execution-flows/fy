"""fy
from typing import List


property mixin_lines: List[str] using flow_file_split:
    property flow_file_split
"""

import abc
from functools import cached_property
from typing import List

from mixins.property.flow_file_split.abc_fy import (
    With_FlowFileSplit_PropertyMixin_ABC,
)


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
