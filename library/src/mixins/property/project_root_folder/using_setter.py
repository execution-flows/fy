# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path


class ProjectRootFolder_PropertyMixin:
    @property
    def _project_root_folder(self) -> Path:
        return self.__project_root_folder

    @_project_root_folder.setter
    def _project_root_folder(self, project_root_folder: Path) -> None:
        self.__project_root_folder = project_root_folder
