import abc

from mixins.property.fy_code.abc import With_FyCode_PropertyMixin_ABC

from domain.parsed_fy_py_file import ParsedFyPyFileKind


class FyFileKind_UsingFyCode_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _fy_file_kind(self) -> ParsedFyPyFileKind:
        return self._fy_file_kind
