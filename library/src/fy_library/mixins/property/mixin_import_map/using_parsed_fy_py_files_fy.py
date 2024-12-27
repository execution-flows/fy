# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property mixin_import_map: Dict[str, str] using parsed_fy_py_files:
    property parsed_fy_py_files
    property required_property_setters_fy_py
    property project_root_folder
"""

import abc
from functools import cached_property
from typing import Dict

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from fy_library.mixins.property.project_root_folder.abc_fy import (
    ProjectRootFolder_PropertyMixin_ABC,
)
from fy_library.mixins.property.required_property_setters_fy_py.abc_fy import (
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
)

from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinImportMap_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    MixinImportMap_PropertyMixin_ABC,
    ParsedFyPyFiles_PropertyMixin_ABC,
    ProjectRootFolder_PropertyMixin_ABC,
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_import_map(self) -> Dict[str, str]:
        # fy:end <<<===
        mixin_import_map = {
            parsed_fy_py_file.entity_key: self.__parsed_file_python_import(
                parsed_fy_py_file
            )
            for parsed_fy_py_file in self._parsed_fy_py_files
            + self._required_property_setters_fy_py
        }
        return mixin_import_map

    def __parsed_file_python_import(self, parsed_fy_py_file: ParsedFyPyFile) -> str:
        relative_file_folder_path = parsed_fy_py_file.file_path.parent.relative_to(
            self._project_root_folder
        )
        file_name = parsed_fy_py_file.file_path.stem
        python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
        return f"from {python_file_path} import {parsed_fy_py_file.python_class_name.pascal_case}"
