from functools import cached_property

import abc

from mixins.property.parsed_fy_files.abc import With_ParsedFyFiles_PropertyMixin_ABC

from typing import Dict

from domain.parsed_fy_file import ParsedFyFile


class ParseFyFilesMapByKey_UsingParsedFyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parse_fy_files_map_by_key(self) -> Dict[str, ParsedFyFile]:
        return {
            parsed_fy_file.template_model.mixin_key: parsed_fy_file
            for parsed_fy_file in self._parsed_fy_files
        }
