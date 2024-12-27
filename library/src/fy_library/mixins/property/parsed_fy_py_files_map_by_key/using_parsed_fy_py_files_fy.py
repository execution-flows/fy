# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
"""

import abc
from functools import cached_property
from typing import Dict

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)

from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        # fy:end <<<===
        return {
            parsed_fy_py_file.entity_key: parsed_fy_py_file
            for parsed_fy_py_file in self._parsed_fy_py_files
        }
