import abc

from mixins.property.fy_py_file_parts.abc import With_FyPyFileParts_PropertyMixin_ABC


class PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _post_marker_file_content(self) -> str:
        post_marker_file_content = self._fy_py_file_parts.post_marker_file_content
        return post_marker_file_content
