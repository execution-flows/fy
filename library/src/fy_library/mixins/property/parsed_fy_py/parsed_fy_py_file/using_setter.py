# fy:start ===>>>
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFile_UsingSetter_PropertyMixin(
    ParsedFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_fy_py_file(self) -> ParsedFyPyFile:
        return self.__parsed_fy_py_file

    @_parsed_fy_py_file.setter
    def _parsed_fy_py_file(self, parsed_fy_py_file: ParsedFyPyFile) -> None:
        self.__parsed_fy_py_file = parsed_fy_py_file


# fy:end <<<===
