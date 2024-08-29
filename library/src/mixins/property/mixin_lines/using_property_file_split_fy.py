"""fy
property mixin_lines: str using property_file_split:
    property property_file_split
"""

import abc
from functools import cached_property

from mixins.property.property_file_split.abc_fy import (
    With_PropertyFileSplit_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinLines_UsingPropertyFileSplit_PropertyMixin(
    # Property_mixins
    With_PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_lines(self) -> str:
        # fy:end <<<===
        return self._property_file_split.mixin_split
