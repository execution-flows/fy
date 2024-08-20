from domain.parsed_fy_py_file import ParsedFyPyFileKind


property fy_file_kind using fy_code:
    with property fy_code

    def -> ParsedFyPyFileKind:
        return self._fy_file_kind
