from domain.parsed_fy_py_file import FyPyFileParts
import abc
import re

from constants import FY_PY_FILE_SIGNATURE, FY_CODE_FILE_END_SIGNATURE


property fy_code using fy_py_file_parts:
    with property fy_py_files_parts

    def -> str:
        fy_code = (self._fy_code.fy_code)
        return fy_code
