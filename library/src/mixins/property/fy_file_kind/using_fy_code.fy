from domain.parsed_fy_py_file import ParsedFyPyFileKind
import re

from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING

property fy_file_kind using fy_code:
    with property fy_py_file_to_parse
    with property fy_code

    def -> ParsedFyPyFileKind:
        flow_match_regex = re.compile(
            rf"^flow\s+{FY_ENTITY_REGEX_STRING}(\s+extends\s+{FY_ENTITY_REGEX_STRING})?\s*"
            rf"->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*$",
        )

        for fy_code_line in self._fy_code.split('\n'):
            if flow_match_regex.match(fy_code_line):
                return ParsedFyPyFileKind.FLOW

        raise ValueError(f"Undetected file type for {self._fy_py_file_to_parse}")
