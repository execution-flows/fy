from functools import cached_property

import abc

from mixins.property.parsed_fy_py_files.abc import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_files_map_by_key.abc import (
    With_ParseFyPyFilesMapByKey_PropertyMixin_ABC,
)

from typing import List

from domain.parsed_fy_py_file import ParsedFyPyFile


class RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    With_ParseFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        return []
