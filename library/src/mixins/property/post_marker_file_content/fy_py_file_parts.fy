property post_marker_file_content using fy_py_file_parts:
    with property fy_py_file_parts

    def -> str:
        post_marker_file_content = self._fy_py_file_parts.post_marker_file_content
        return post_marker_file_content
