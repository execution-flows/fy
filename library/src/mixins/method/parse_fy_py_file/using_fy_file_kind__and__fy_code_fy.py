"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


method parse_fy_py_file -> ParsedFyPyFile using fy_file_kind__and__fy_code:
    with property fy_py_file_to_parse
    with property fy_code
    with property pre_marker_file_content
    with property post_marker_file_content
    with property fy_file_kind
"""

from base.flow_base import FlowBase
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from flows.parse_abstract_method_fy_code_fy import ParseAbstractMethodFyCode_Flow
from flows.parse_abstract_property_fy_code_fy import ParseAbstractPropertyFyCode_Flow
from flows.parse_flow_fy_code_fy import ParseFlowFyCode_Flow
from flows.parse_method_fy_code_fy import ParseMethodFyCode_Flow
from flows.parse_property_fy_code_fy import ParsePropertyFyCode_Flow
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_file_kind.abc_fy import (
    With_FyFileKind_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc_fy import (
    With_PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.pre_marker_file_content.abc_fy import (
    With_PreMarkerFileContent_PropertyMixin_ABC,
)
import abc


# fy:start <<<===
class ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin(
    # Property_mixins
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyFileKind_PropertyMixin_ABC,
    abc.ABC,
):
    def _parse_fy_py_file(self) -> ParsedFyPyFile:
        # fy:end <<<===
        parse_fy_code: FlowBase[ParsedFyPyFile]
        match self._fy_file_kind:
            case ParsedFyPyFileKind.FLOW:
                parse_fy_code = ParseFlowFyCode_Flow(
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.METHOD:
                parse_fy_code = ParseMethodFyCode_Flow(
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                parse_fy_code = ParseAbstractMethodFyCode_Flow(
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                parse_fy_code = ParseAbstractPropertyFyCode_Flow(
                    fy_code=self._fy_code,
                    pre_marker_file_content=self._pre_marker_file_content,
                    post_marker_file_content=self._post_marker_file_content,
                    fy_py_file_to_parse=self._fy_py_file_to_parse,
                )
            case ParsedFyPyFileKind.PROPERTY:
                parse_fy_code = ParsePropertyFyCode_Flow(
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