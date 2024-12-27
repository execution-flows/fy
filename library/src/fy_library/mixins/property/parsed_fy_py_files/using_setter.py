# fy:start ===>>>
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFiles_UsingSetter_PropertyMixin:
    @property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        return self.__parsed_fy_py_files

    @_parsed_fy_py_files.setter
    def _parsed_fy_py_files(self, parsed_fy_py_files: List[ParsedFyPyFile]) -> None:
        self.__parsed_fy_py_files = parsed_fy_py_files


# fy:end <<<===
