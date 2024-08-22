property fy_code using fy_py_file_parts:
    with property fy_py_file_parts

    def -> str:
        fy_code = self._fy_py_file_parts.fy_code
        return fy_code
