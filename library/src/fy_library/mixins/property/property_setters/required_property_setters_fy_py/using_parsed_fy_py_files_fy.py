# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


property required_property_setters_fy_py: List[PropertySetterFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
    property parsed_fy_py_files_map_by_key
    property required_setters
fy"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.parsed_fy_py_file import (
    PropertySetterFyPyFile,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.required_property_setters_fy_py.abc_fy import (
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.required_setters.abc_fy import (
    RequiredSetters_PropertyMixin_ABC,
)


# fy:start ===>>>
class RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin(
    # Property Mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
    RequiredSetters_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_property_setters_fy_py(self) -> List[PropertySetterFyPyFile]:
        # fy:end <<<===
        required_setters = self._required_setters
        return list(required_setters.values())
