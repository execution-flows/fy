from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from flows.parse_flow_fy_code import ParseFlowFyCode_Flow
from base.execution_flow_base import ExecutionFlowBase
from flows.parse_method_fy_code import ParseMethodFyCode_Flow


method parse_fy_py_file using fy_file_kind__and__fy_code:
    with property fy_py_file_to_parse
    with property fy_code
    with property pre_marker_file_content
    with property post_marker_file_content
    with property fy_file_kind

    def -> ParsedFyPyFile:
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
            case _:
                raise NotImplementedError(
                    f"Unimplemented fy file kind parser for {self._fy_file_kind}"
                )

        return parse_fy_code()
