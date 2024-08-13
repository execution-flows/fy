# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path


class FolderToParse_PropertyMixin:
    @property
    def _folder_to_parse(self) -> Path:
        return self.__folder_to_parse

    @_folder_to_parse.setter
    def _folder_to_parse(self, folder_to_parse: Path) -> None:
        self.__folder_to_parse = folder_to_parse
