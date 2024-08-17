from pathlib import Path


property project_root_folder using setter:
    def -> Path:
        return self._project_root_folder

    @_project_root_folder.setter
    def _project_root_folder(self, project_root_folder: Path) -> None:
        self.__project_root_folder = project_root_folder
