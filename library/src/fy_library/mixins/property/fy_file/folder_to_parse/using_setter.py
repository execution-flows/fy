# fy:start ===>>>
from fy_library.mixins.property.fy_file.folder_to_parse.abc_fy import (
    FolderToParse_PropertyMixin_ABC,
)
from pathlib import Path


class FolderToParse_UsingSetter_PropertyMixin(
    FolderToParse_PropertyMixin_ABC,
):
    @property
    def _folder_to_parse(self) -> Path:
        return self.__folder_to_parse

    @_folder_to_parse.setter
    def _folder_to_parse(self, folder_to_parse: Path) -> None:
        self.__folder_to_parse = folder_to_parse


# fy:end <<<===
