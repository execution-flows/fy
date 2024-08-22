import abc

from mixins.property.fy_py_file_to_parse.abc import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)

import re

from constants import FY_PY_FILE_SIGNATURE, FY_CODE_FILE_END_SIGNATURE
from domain.parsed_fy_py_file import FyPyFileParts


class FyPyFilesParts_UsingFyFileToParseDocstring_PropertyMixin(
    # Property_mixins
    With_FyPyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _fy_py_files_parts(self) -> FyPyFileParts:
        fy_code_regex = re.compile(
            rf"^{FY_PY_FILE_SIGNATURE}"
            rf"(?P<fy_code>.*)"
            rf"{FY_CODE_FILE_END_SIGNATURE}",
            flags=re.DOTALL,
        )

        with open(file=self._fy_py_file_to_parse, mode="r") as fy_py_file:
            content = fy_py_file.read()

        fy_code_regex_search = fy_code_regex.search(content)
        fy_code = fy_code_regex_search.group("fy_code")

        fy_py_file_parts = FyPyFileParts(
            fy_code=fy_code,
            pre_marker="",
            post_marker="",
        )

        return fy_py_file_parts
