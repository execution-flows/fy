import abc

from mixins.property.fy_py_file_to_parse.abc import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)


class FyCode_UsingFyFileToParseDocstring_PropertyMixin(
    # Property_mixins
    With_FyPyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _fy_code(self) -> str:
        return ""
