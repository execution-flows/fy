# fy:start ===>>>
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class FilesToGenerate_UsingSetter_PropertyMixin:
    @property
    def _files_to_generate(self) -> list[ParsedFyPyFile]:
        return self.__files_to_generate

    @_files_to_generate.setter
    def _files_to_generate(self, files_to_generate: list[ParsedFyPyFile]) -> None:
        self.__files_to_generate = files_to_generate


# fy:end <<<===
