import abc

from mixins.property.fy_py_file_to_parse.abc import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc_fy import With_FyCode_PropertyMixin_ABC
from mixins.property.pre_marker_file_content.abc import (
    With_PreMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc import (
    With_PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.fy_file_kind.abc_fy import With_FyFileKind_PropertyMixin_ABC

from flows.parse_property_fy_code import ParsePropertyFyCode_Flow
from flows.parse_abstract_method_fy_code import ParseAbstractMethodFyCode_Flow
from flows.parse_abstract_property_fy_code import ParseAbstractPropertyFyCode_Flow
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from flows.parse_flow_fy_code import ParseFlowFyCode_Flow
from base.execution_flow_base import ExecutionFlowBase
from flows.parse_method_fy_code import ParseMethodFyCode_Flow


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
        parse_fy_code: ExecutionFlowBase[ParsedFyPyFile]
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
