# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files: List[ParsedFyPyFile] using fy_py_parser:
    property fy_py_files_to_parse
"""

import abc
from functools import cached_property
from typing import List

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.flows.parse_fy_py_file_fy import ParseFyPyFile_Flow
from fy_library.mixins.property.fy_py_files_to_parse.abc_fy import (
    FyPyFilesToParse_PropertyMixin_ABC,
)

from fy_library.mixins.property.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFiles_UsingFyPyParser_PropertyMixin(
    # Property_mixins
    FyPyFilesToParse_PropertyMixin_ABC,
    ParsedFyPyFiles_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        return [
            ParseFyPyFile_Flow(fy_py_file_to_parse=fy_py_file)()
            for fy_py_file in self._fy_py_files_to_parse
        ]
