# fy:start ===>>>
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


class BaseFlowRequiredPropertySettersFyPy_UsingSetter_PropertyMixin:
    @property
    def _base_flow_required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        return self.__base_flow_required_property_setters_fy_py

    @_base_flow_required_property_setters_fy_py.setter
    def _base_flow_required_property_setters_fy_py(self, base_flow_required_property_setters_fy_py: List[ParsedFyPyFile]) -> None:
        self.__base_flow_required_property_setters_fy_py = base_flow_required_property_setters_fy_py
        # fy:end <<<===
