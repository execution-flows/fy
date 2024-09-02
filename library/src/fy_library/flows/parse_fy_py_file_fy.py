# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseFyPyFile -> ParsedFyPyFile:
    property fy_py_file_to_parse using setter
    property fy_py_file_parts using fy_file_to_parse_docstring
    property pre_fy_code using fy_py_file_parts
    property fy_code using fy_py_file_parts
    property post_marker_file_content using fy_py_file_parts
    property pre_marker_file_content using fy_py_file_parts
    property fy_file_kind using fy_code

    method parse_fy_py_file using fy_file_kind__and__fy_code
"""

from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.method.parse_fy_py_file.using_fy_file_kind__and__fy_code_fy import (
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
)
from fy_library.mixins.property.fy_code.using_fy_py_file_parts_fy import (
    FyCode_UsingFyPyFileParts_PropertyMixin,
)
from fy_library.mixins.property.fy_file_kind.using_fy_code_fy import (
    FyFileKind_UsingFyCode_PropertyMixin,
)
from fy_library.mixins.property.fy_py_file_parts.using_fy_file_to_parse_docstring_fy import (
    FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin,
)
from fy_library.mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.post_marker_file_content.using_fy_py_file_parts_fy import (
    PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
)
from fy_library.mixins.property.pre_fy_code.using_fy_py_file_parts_fy import (
    PreFyCode_UsingFyPyFileParts_PropertyMixin,
)
from fy_library.mixins.property.pre_marker_file_content.using_fy_py_file_parts_fy import (
    PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
)


# fy:start ===>>>
class ParseFyPyFile_Flow(
    # Property Mixins
    FyPyFileToParse_UsingSetter_PropertyMixin,
    FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin,
    PreFyCode_UsingFyPyFileParts_PropertyMixin,
    FyCode_UsingFyPyFileParts_PropertyMixin,
    PostMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
    PreMarkerFileContent_UsingFyPyFileParts_PropertyMixin,
    FyFileKind_UsingFyCode_PropertyMixin,
    # Method Mixins
    ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __init__(
        self,
        *args: Any,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        return self._parse_fy_py_file()
