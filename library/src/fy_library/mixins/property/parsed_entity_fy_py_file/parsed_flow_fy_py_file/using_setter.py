# fy:start ===>>>
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_flow_fy_py_file.abc_fy import (
    ParsedFlowFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile


class ParsedFlowFyPyFile_UsingSetter_PropertyMixin(
    ParsedFlowFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_flow_fy_py_file(self) -> ParsedFlowFyPyFile:
        return self.__parsed_flow_fy_py_file

    @_parsed_flow_fy_py_file.setter
    def _parsed_flow_fy_py_file(
        self, parsed_flow_fy_py_file: ParsedFlowFyPyFile
    ) -> None:
        self.__parsed_flow_fy_py_file = parsed_flow_fy_py_file


# fy:end <<<===
