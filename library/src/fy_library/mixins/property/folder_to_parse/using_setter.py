# fy:start ===>>>
from pathlib import Path


class FolderToParse_UsingSetter_PropertyMixin:
    @property
    def _folder_to_parse(self) -> Path:
        return self.__folder_to_parse

    @_folder_to_parse.setter
    def _folder_to_parse(self, folder_to_parse: Path) -> None:
        self.__folder_to_parse = folder_to_parse


# fy:end <<<===
