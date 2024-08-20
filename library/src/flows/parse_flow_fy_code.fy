from domain.parsed_fy_py_file import ParsedFyPyFile
from typing import Any


flow ParseFlowFyCode:
    property fy_code using setter

    def -> ParsedFyPyFile:
        return ParsedFyPyFile()

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        super().__init__(*args, **kwargs)
