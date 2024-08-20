import abc

from mixins.property.fy_code.abc import With_FyCode_PropertyMixin_ABC
from mixins.property.fy_file_kind.abc import With_FyFileKind_PropertyMixin_ABC

from domain.parsed_fy_py_file import ParsedFyPyFile


class ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_FyFileKind_PropertyMixin_ABC,
    abc.ABC,
):
    def _parse_fy_py_file(self) -> ParsedFyPyFile:
        print(self._fy_code)
        return ParsedFyPyFile()
