# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFile_UsingSetter_PropertyMixin:
    @property
    def _parsed_fy_py_file(self) -> ParsedFyPyFile:
        return self.__parsed_fy_py_file

    @_parsed_fy_py_file.setter
    def _parsed_fy_py_file(self, parsed_fy_py_file: ParsedFyPyFile) -> None:
        self.__parsed_fy_py_file = parsed_fy_py_file


# fy:end <<<===
