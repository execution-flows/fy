"""fy
property pre_marker_file_content: str using fy_py_file_parts:
    property fy_py_file_parts
"""

import abc
from functools import cached_property


from mixins.property.fy_py_file_parts.abc_fy import (
    FyPyFileParts_PropertyMixin_ABC,
)


# fy:start ===>>>
class PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _pre_marker_file_content(self) -> str:
        # fy:end <<<===
        pre_marker_file_content = self._fy_py_file_parts.pre_marker_file_content
        return pre_marker_file_content
