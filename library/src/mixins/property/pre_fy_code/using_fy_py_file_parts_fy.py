"""fy
property pre_fy_code: str using fy_py_file_parts:
    property fy_py_file_parts
"""

from functools import cached_property
from mixins.property.fy_py_file_parts.abc_fy import (
    FyPyFileParts_PropertyMixin_ABC,
)
import abc


# fy:start ===>>>
class PreFyCode_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _pre_fy_code(self) -> str:
        # fy:end <<<===
        return self._fy_py_file_parts.pre_fy_code
