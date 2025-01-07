# fy:start ===>>>
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_method_fy_py_file.abc_fy import (
    ParsedMethodFyPyFile_PropertyMixin_ABC,
)
from fy_library.domain.parsed_fy_py_file import ParsedMethodFyPyFile


class ParsedMethodFyPyFile_UsingSetter_PropertyMixin(
    ParsedMethodFyPyFile_PropertyMixin_ABC,
):
    @property
    def _parsed_method_fy_py_file(self) -> ParsedMethodFyPyFile:
        return self.__parsed_method_fy_py_file

    @_parsed_method_fy_py_file.setter
    def _parsed_method_fy_py_file(
        self, parsed_method_fy_py_file: ParsedMethodFyPyFile
    ) -> None:
        self.__parsed_method_fy_py_file = parsed_method_fy_py_file


# fy:end <<<===
