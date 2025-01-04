# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind


class ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin:
    @property
    def _parsed_fy_py_files_map_by_key(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], ParsedFyPyFile]:
        return self.__parsed_fy_py_files_map_by_key

    @_parsed_fy_py_files_map_by_key.setter
    def _parsed_fy_py_files_map_by_key(
        self,
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
    ) -> None:
        self.__parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key


# fy:end <<<===
