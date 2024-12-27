# fy:start ===>>>
class PostMarkerFileContent_UsingSetter_PropertyMixin:
    @property
    def _post_marker_file_content(self) -> str:
        return self.__post_marker_file_content

    @_post_marker_file_content.setter
    def _post_marker_file_content(self, post_marker_file_content: str) -> None:
        self.__post_marker_file_content = post_marker_file_content


# fy:end <<<===
