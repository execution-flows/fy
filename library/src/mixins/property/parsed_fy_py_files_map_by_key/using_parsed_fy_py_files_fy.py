"""fy
from typing import Dict
from domain.parsed_fy_py_file import ParsedFyPyFile

@cached
property parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
"""

import abc
from functools import cached_property
from typing import Dict

from domain.parsed_fy_py_file import ParsedFyPyFile


from mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        # fy:end <<<===
        return {
            parsed_fy_py_file.template_model.entity_key: parsed_fy_py_file
            for parsed_fy_py_file in self._parsed_fy_py_files
        }
