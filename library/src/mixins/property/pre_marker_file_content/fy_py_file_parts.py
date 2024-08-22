import abc

from mixins.property.fy_py_file_parts.abc import With_FyPyFileParts_PropertyMixin_ABC


class PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _pre_marker_file_content(self) -> str:
        pre_marker_file_content = self._fy_py_file_parts.pre_marker_file_content
        return pre_marker_file_content
