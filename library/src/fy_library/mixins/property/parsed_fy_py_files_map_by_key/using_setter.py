# fy:start ===>>>
from typing import Dict
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin:
    @property
    def _parsed_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        return self.__parsed_fy_py_files_map_by_key

    @_parsed_fy_py_files_map_by_key.setter
    def _parsed_fy_py_files_map_by_key(
        self, parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile]
    ) -> None:
        self.__parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key


# fy:end <<<===
