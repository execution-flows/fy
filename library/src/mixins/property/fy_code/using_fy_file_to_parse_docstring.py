import abc

from mixins.property.fypy_file_to_parse.abc import (
    With_FypyFileToParse_PropertyMixin_ABC,
)


class FyCode_UsingFyFileToParseDocstring_PropertyMixin(
    # Property_mixins
    With_FypyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _fy_code(self) -> str:
        return ""
