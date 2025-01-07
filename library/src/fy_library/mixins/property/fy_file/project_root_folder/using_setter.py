# fy:start ===>>>
from fy_library.mixins.property.fy_file.project_root_folder.abc_fy import (
    ProjectRootFolder_PropertyMixin_ABC,
)
from pathlib import Path


class ProjectRootFolder_UsingSetter_PropertyMixin(
    ProjectRootFolder_PropertyMixin_ABC,
):
    @property
    def _project_root_folder(self) -> Path:
        return self.__project_root_folder

    @_project_root_folder.setter
    def _project_root_folder(self, project_root_folder: Path) -> None:
        self.__project_root_folder = project_root_folder


# fy:end <<<===
