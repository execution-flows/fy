from functools import cached_property

import abc

from mixins.property.fy_py_files_to_parse.abc import (
    With_FyPyFilesToParse_PropertyMixin_ABC,
)

from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile


class ParsedFyPyFiles_UsingFyPyParser_PropertyMixin(
    # Property_mixins
    With_FyPyFilesToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        return []
