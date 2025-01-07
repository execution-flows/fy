# fy:start ===>>>
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_property_fy_py_file.abc_fy import (
    ParsedPropertyFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile


class ParsedPropertyFyPyFile_UsingSetter_PropertyMixin(
    ParsedPropertyFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        return self.__parsed_property_fy_py_file

    @_parsed_property_fy_py_file.setter
    def _parsed_property_fy_py_file(
        self, parsed_property_fy_py_file: ParsedPropertyFyPyFile
    ) -> None:
        self.__parsed_property_fy_py_file = parsed_property_fy_py_file


# fy:end <<<===
