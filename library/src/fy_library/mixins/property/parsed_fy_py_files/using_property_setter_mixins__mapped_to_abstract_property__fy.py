# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files: List[ParsedFyPyFile] using property_setter_mixins__mapped_to_abstract_property:
    property property_setter_mixins
    property parsed_fy_py_files_map_by_key
"""

from functools import cached_property
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setter_mixins.abc_fy import (
    PropertySetterMixins_PropertyMixin_ABC,
)
from typing import List
import abc

from fy_library.mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    PropertySetterMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        return [
            self._parsed_fy_py_files_map_by_key[
                property_setter.property_name.snake_case
            ]
            for property_setter in self._property_setter_mixins
        ]
