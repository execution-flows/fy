"""fy
property mixin_lines: str using method_file_split:
    property method_file_split
"""

import abc
from functools import cached_property

from mixins.property.method_file_split.abc_fy import (
    With_MethodFileSplit_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinLines_UsingMethodFileSplit_PropertyMixin(
    # Property_mixins
    With_MethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_lines(self) -> str:
        # fy:end <<<===
        return self._method_file_split.mixin_split
