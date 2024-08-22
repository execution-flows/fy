import abc

from mixins.property.fy_py_file_to_parse.abc import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc import With_FyCode_PropertyMixin_ABC
from mixins.property.fy_file_kind.abc import With_FyFileKind_PropertyMixin_ABC

from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFyPyFileKind
from flows.parse_flow_fy_code import ParseFlowFyCode_Flow


class ParseFyPyFile_UsingFyFileKind_And_FyCode_MethodMixin(
    # Property_mixins
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_FyCode_PropertyMixin_ABC,
    With_FyFileKind_PropertyMixin_ABC,
    abc.ABC,
):
    def _parse_fy_py_file(self) -> ParsedFyPyFile:
        match self._fy_file_kind:
            case ParsedFyPyFileKind.FLOW:
                parse_fy_code = ParseFlowFyCode_Flow(
                    fy_code=self._fy_code, fy_py_file_path=self._fy_py_file_to_parse
                )
            case _:
                raise NotImplementedError(
                    f"Unimplemented fy file kind parser for {self._fy_file_kind}"
                )

        return parse_fy_code()
