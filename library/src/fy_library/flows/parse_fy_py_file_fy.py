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
"""

from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from fy_library.flows.parse_abstract_method_fy_code_fy import (
    ParseAbstractMethodFyCode_Flow,
)
from fy_library.flows.parse_abstract_property_fy_code_fy import (
    ParseAbstractPropertyFyCode_Flow,
)
from fy_library.flows.parse_base_flow_fy_code_fy import ParseBaseFlowFyCode_Flow
from fy_library.flows.parse_flow_fy_code_fy import ParseFlowFyCode_Flow
from fy_library.flows.parse_method_fy_code_fy import ParseMethodFyCode_Flow
from fy_library.flows.parse_property_fy_code_fy import ParsePropertyFyCode_Flow
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
        parse_fy_code: FlowBase[ParsedFyPyFile]
        match self._fy_file_kind:
            case ParsedFyPyFileKind.FLOW:
                parse_fy_code = ParseFlowFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.BASE_FLOW:
                parse_fy_code = ParseBaseFlowFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.METHOD:
                parse_fy_code = ParseMethodFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                parse_fy_code = ParseAbstractMethodFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                parse_fy_code = ParseAbstractPropertyFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.PROPERTY:
                parse_fy_code = ParsePropertyFyCode_Flow(
                    pre_fy_code=self._pre_fy_code,
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case _:
                raise NotImplementedError(
                    f"Unimplemented fy file kind parser for {self._fy_file_kind}"
                )

        return parse_fy_code()
