from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from flows.parse_flow_fy_code import ParseFlowFyCode_Flow


method parse_fy_py_file using fy_file_kind__and__fy_code:
    with property fy_py_file_to_parse
    with property fy_code
    with property fy_file_kind

    def -> ParsedFyPyFile:
        match self._fy_file_kind:
            case ParsedFyPyFileKind.FLOW:
                parse_fy_code = ParseFlowFyCode_Flow(fy_code=self._fy_code, fy_py_file_path=self._fy_py_file_to_parse)
            case _:
                raise NotImplementedError(f"Unimplemented fy file kind parser for {self._fy_file_kind}")

        return parse_fy_code()
