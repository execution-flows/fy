# fy:start ===>>>
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_base_flow_fy_py_file.abc_fy import (
    ParsedBaseFlowFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedBaseFlowFyPyFile


class ParsedBaseFlowFyPyFile_UsingSetter_PropertyMixin(
    ParsedBaseFlowFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_base_flow_fy_py_file(self) -> ParsedBaseFlowFyPyFile:
        return self.__parsed_base_flow_fy_py_file

    @_parsed_base_flow_fy_py_file.setter
    def _parsed_base_flow_fy_py_file(
        self, parsed_base_flow_fy_py_file: ParsedBaseFlowFyPyFile
    ) -> None:
        self.__parsed_base_flow_fy_py_file = parsed_base_flow_fy_py_file


# fy:end <<<===
