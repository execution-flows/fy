"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseMethodFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property method_file_split using method_regex
    property declared_abstract_property_mixins using method_file_split
    property declared_abstract_method_mixins using method_file_split
    property parsed_method_fy_py_file using parsed_fy_py_file
"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import ParsedFyPyFile
from mixins.property.declared_abstract_property_mixins.using_method_file_split_fy import (
    DeclaredAbstractPropertyMixins_UsingMethodFileSplit_PropertyMixin,
)
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.method_file_split.using_method_regex_fy import (
    MethodFileSplit_UsingMethodRegex_PropertyMixin,
)
from mixins.property.parsed_method_fy_py_file.parsed_fy_py_file_fy import (
    ParsedMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)


from mixins.property.declared_abstract_method_mixins.using_method_file_split_fy import (
    DeclaredAbstractMethodMixins_UsingMethodFileSplit_PropertyMixin,
)


# fy:start <<<===
class ParseMethodFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    MethodFileSplit_UsingMethodRegex_PropertyMixin,
    DeclaredAbstractPropertyMixins_UsingMethodFileSplit_PropertyMixin,
    DeclaredAbstractMethodMixins_UsingMethodFileSplit_PropertyMixin,
    ParsedMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        return self._parsed_method_fy_py_file

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
