from functools import cached_property

import abc

from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC
from mixins.property.required_property_setters.abc import (
    With_RequiredPropertySetters_PropertyMixin_ABC,
)
from mixins.property.project_root_folder.abc_fy import (
    With_ProjectRootFolder_PropertyMixin_ABC,
)

from typing import Dict

from domain.parsed_fy_file import ParsedFyFile


class MixinImportMap_UsingParsedFyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyFiles_PropertyMixin_ABC,
    With_RequiredPropertySetters_PropertyMixin_ABC,
    With_ProjectRootFolder_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_import_map(self) -> Dict[str, str]:
        mixin_import_map = {
            parsed_fy_file.template_model.entity_key: self.__parsed_file_python_import(
                parsed_fy_file
            )
            for parsed_fy_file in self._parsed_fy_files
            + self._required_property_setters
        }
        return mixin_import_map

    def __parsed_file_python_import(self, parsed_fy_file: ParsedFyFile) -> str:
        relative_file_folder_path = (
            parsed_fy_file.output_py_file_path.parent.relative_to(
                self._project_root_folder
            )
        )
        file_name = parsed_fy_file.output_py_file_path.stem
        python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
        return f"from {python_file_path} import {parsed_fy_file.template_model.python_class_name.pascal_case}"
