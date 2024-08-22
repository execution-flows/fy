import abc

from mixins.property.fy_py_files_parts.abc import With_FyPyFileParts_PropertyMixin_ABC


class FyCode_UsingFyPyFileParts_PropertyMixin(
    # Property_mixins
    With_FyPyFileParts_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _fy_code(self) -> str:
        fy_code = self._fy_py_file_parts.fy_code
        return fy_code
