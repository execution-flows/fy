"""fy
import re
from constants import FY_PY_FILE_SIGNATURE, FY_CODE_FILE_END_SIGNATURE, FY_START_MARKER, FY_END_MARKER
from domain.parsed_fy_py_file import FyPyFileParts


@cached
property fy_py_file_parts: FyPyFileParts using fy_file_to_parse_docstring:
    with property fy_py_file_to_parse
"""

from constants import (
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from domain.parsed_fy_py_file import FyPyFileParts
from functools import cached_property
from mixins.property.fy_py_file_to_parse.abc_fy import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
import abc
import re


# fy:start <<<===
class FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin(
    # Property_mixins
    With_FyPyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_parts(self) -> FyPyFileParts:
        # fy:end <<<===
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

        non_fy_code = content[
            len(f"{FY_PY_FILE_SIGNATURE}{fy_code}{FY_CODE_FILE_END_SIGNATURE}\n"):  # fmt: skip
        ]

        pre_marker_file_content = non_fy_code.split(f"{FY_START_MARKER}\n")[0]
        post_marker_file_content = non_fy_code.split(f"{FY_END_MARKER}\n")[-1]

        fy_py_file_parts = FyPyFileParts(
            fy_code=fy_code,
            pre_marker_file_content=pre_marker_file_content,
            post_marker_file_content=post_marker_file_content,
        )

        return fy_py_file_parts
