"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseAbstractPropertyFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property abstract_property_file_split using abstract_property_regex
    property parsed_abstract_property_fy_py_file using parsed_fy_py_file

"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import ParsedFyPyFile

from mixins.property.abstract_property_file_split.using_abstract_property_regex_fy import (
    AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin,
)
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.parsed_abstract_property_fy_py_file.parsed_fy_py_file_fy import (
    ParsedAbstractPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)


# fy:start <<<===
class ParseAbstractPropertyFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin,
    ParsedAbstractPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        return self._parsed_abstract_property_fy_py_file

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
