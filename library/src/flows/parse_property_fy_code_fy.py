"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParsePropertyFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property property_file_split using property_regex
    property property_mixins using mixin_lines
    property parsed_property_fy_py_file using parsed_fy_py_file
"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import ParsedFyPyFile
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.parsed_property_fy_py_file.using_parsed_fy_py_file_fy import (
    ParsedPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.property_file_split.usign_property_regex_fy import (
    PropertyFileSplit_UsingPropertyRegex_PropertyMixin,
)
from mixins.property.property_mixins.using_mixin_lines_fy import (
    PropertyMixins_UsingMixinLines_PropertyMixin,
)


# fy:start <<<===
class ParsePropertyFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    PropertyFileSplit_UsingPropertyRegex_PropertyMixin,
    PropertyMixins_UsingMixinLines_PropertyMixin,
    ParsedPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        return self._parsed_property_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        pre_marker_file_content: str,
        post_marker_file_content: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        self._fy_py_file_to_parse = fy_py_file_to_parse
        self._pre_marker_file_content = pre_marker_file_content
        self._post_marker_file_content = post_marker_file_content
        super().__init__(*args, **kwargs)
