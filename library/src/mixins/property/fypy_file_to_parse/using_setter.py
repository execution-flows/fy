from pathlib import Path


class FypyFileToParse_UsingSetter_PropertyMixin:
    @property
    def _fypy_file_to_parse(self) -> Path:
        return self.__fypy_file_to_parse

    @_fypy_file_to_parse.setter
    def _fypy_file_to_parse(self, fypy_file_to_parse: Path) -> None:
        self.__fypy_file_to_parse = fypy_file_to_parse
