flow ParseFyPyFile:
    property fy_py_file_to_parse using setter
    property fy_code using fy_file_to_parse_docstring
    property fy_file_kind using fy_code

    method parse_fy_py_file using fy_file_kind__and__fy_code

    def -> None:
        self._parse_fy_py_file()
