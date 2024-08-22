property pre_marker_file_content using fy_py_file_parts:
    with property fy_py_file_parts

    def -> str:
        pre_marker_file_content = self._fy_py_file_parts.pre_marker_file_content
        return pre_marker_file_content
