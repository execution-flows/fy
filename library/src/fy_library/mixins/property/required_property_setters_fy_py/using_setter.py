# fy:start ===>>>
from typing import List
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


class RequiredPropertySettersFyPy_UsingSetter_PropertyMixin:
    @property
    def _required_property_setters_fy_py(self) -> List[PropertySetterFyPyFile]:
        return self.__required_property_setters_fy_py

    @_required_property_setters_fy_py.setter
    def _required_property_setters_fy_py(
        self, required_property_setters_fy_py: List[PropertySetterFyPyFile]
    ) -> None:
        self.__required_property_setters_fy_py = required_property_setters_fy_py


# fy:end <<<===
