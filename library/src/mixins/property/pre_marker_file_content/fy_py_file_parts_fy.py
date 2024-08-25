"""fy
property pre_marker_file_content: str using fy_py_file_parts:
    with property fy_py_file_parts
"""

from mixins.property.fy_py_file_parts.abc_fy import (
    With_FyPyFileParts_PropertyMixin_ABC,
)
import abc


# fy:start <<<===
class PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _pre_marker_file_content(self) -> str:
        # fy:end <<<===
        pre_marker_file_content = self._fy_py_file_parts.pre_marker_file_content
        return pre_marker_file_content
