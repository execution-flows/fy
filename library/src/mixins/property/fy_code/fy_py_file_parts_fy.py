"""fy
property fy_code: str using fy_py_file_parts:
    property fy_py_file_parts
"""

import abc
from functools import cached_property

from mixins.property.fy_py_file_parts.abc_fy import (
    With_FyPyFileParts_PropertyMixin_ABC,
)


# fy:start ===>>>
class FyCode_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_code(self) -> str:
        # fy:end <<<===
        fy_code = self._fy_py_file_parts.fy_code
        return fy_code
