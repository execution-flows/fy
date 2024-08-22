from pathlib import Path
from typing import Any

from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseFyPyFile:
    property fy_py_file_to_parse using setter
    property fy_py_file_parts using fy_file_to_parse_docstring
    property fy_code using fy_py_file_parts
    property fy_file_kind using fy_code

    method parse_fy_py_file using fy_file_kind__and__fy_code

    def -> ParsedFyPyFile:
        return self._parse_fy_py_file()

    def __init__(
        self,
        *args: Any,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_py_file_to_parse = fy_py_file_to_parse
        super().__init__(*args, **kwargs)
