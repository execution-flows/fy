from domain.parsed_fy_py_file import ParsedFyPyFile


method parse_fy_py_file using fy_file_kind__and__fy_code:
    with property fy_code
    with property fy_file_kind

    def -> ParsedFyPyFile:
        print(self._fy_code)
        print(self._fy_file_kind)
        return self._parse_fy_py_file()
