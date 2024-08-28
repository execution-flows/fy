"""fy
property post_marker_file_content: str using fy_py_file_parts:
    property fy_py_file_parts
"""

from mixins.property.fy_py_file_parts.abc_fy import (
    With_FyPyFileParts_PropertyMixin_ABC,
)
import abc


from functools import cached_property


# fy:start <<<===
class PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _post_marker_file_content(self) -> str:
        # fy:end <<<===
        post_marker_file_content = self._fy_py_file_parts.post_marker_file_content
        return post_marker_file_content
