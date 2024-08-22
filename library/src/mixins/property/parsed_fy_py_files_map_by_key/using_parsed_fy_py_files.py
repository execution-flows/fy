from functools import cached_property

import abc

from mixins.property.parsed_fy_py_files.abc import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)

from typing import Dict

from domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        return {
            parsed_fy_py_file.template_model.entity_key: parsed_fy_py_file
            for parsed_fy_py_file in self._parsed_fy_py_files
        }
