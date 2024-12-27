# fy:start ===>>>
from pathlib import Path


class FyPyFileToParse_UsingSetter_PropertyMixin:
    @property
    def _fy_py_file_to_parse(self) -> Path:
        return self.__fy_py_file_to_parse

    @_fy_py_file_to_parse.setter
    def _fy_py_file_to_parse(self, fy_py_file_to_parse: Path) -> None:
        self.__fy_py_file_to_parse = fy_py_file_to_parse


# fy:end <<<===
