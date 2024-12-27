# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import FyPyFileParts


property fy_py_file_parts: FyPyFileParts using fy_file_to_parse_docstring:
    property fy_py_file_to_parse
"""

import abc
import re
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from fy_library.domain.parsed_fy_py_file import FyPyFileParts
from fy_library.mixins.property.fy_py_file_parts.abc_fy import (
    FyPyFileParts_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)

_FY_CODE_REGEX: Final = re.compile(
    rf"^(?P<pre_fy_code>\s*#.*\n)*"
    rf"{FY_PY_FILE_SIGNATURE}"
    rf"(?P<fy_code>.*)"
    rf"{FY_CODE_FILE_END_SIGNATURE}",
    flags=re.DOTALL,
)
_FY_END_MARKER_REGEX: Final = re.compile(rf"\s*{FY_END_MARKER}\n")


# fy:start ===>>>
class FyPyFileParts_UsingFyFileToParseDocstring_PropertyMixin(
    # Property_mixins
    FyPyFileParts_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _fy_py_file_parts(self) -> FyPyFileParts:
        # fy:end <<<===
        with open(file=self._fy_py_file_to_parse, mode="r") as fy_py_file:
            content = fy_py_file.read()

        fy_code_regex_search = _FY_CODE_REGEX.search(content)
        pre_fy_code = fy_code_regex_search.group("pre_fy_code") or ""
        fy_code = fy_code_regex_search.group("fy_code")

        non_fy_code = content[
            len(
                f"{pre_fy_code}{FY_PY_FILE_SIGNATURE}{fy_code}{FY_CODE_FILE_END_SIGNATURE}\n"
            ) :  # fmt: skip
        ]

        pre_marker_file_content = non_fy_code.split(f"{FY_START_MARKER}\n")[0]
        post_marker_file_content = _FY_END_MARKER_REGEX.split(non_fy_code)[-1]

        fy_py_file_parts = FyPyFileParts(
            pre_fy_code=pre_fy_code,
            fy_code=fy_code,
            pre_marker_file_content=pre_marker_file_content,
            post_marker_file_content=post_marker_file_content,
        )

        return fy_py_file_parts
