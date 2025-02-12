# fy:start ===>>>
from pathlib import Path


class FolderToGenerate_UsingSetter_PropertyMixin:
    @property
    def _folder_to_generate(self) -> Path:
        return self.__folder_to_generate

    @_folder_to_generate.setter
    def _folder_to_generate(self, folder_to_generate: Path) -> None:
        self.__folder_to_generate = folder_to_generate


# fy:end <<<===
