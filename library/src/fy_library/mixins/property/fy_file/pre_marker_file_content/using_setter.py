# fy:start ===>>>
class PreMarkerFileContent_UsingSetter_PropertyMixin:
    @property
    def _pre_marker_file_content(self) -> str:
        return self.__pre_marker_file_content

    @_pre_marker_file_content.setter
    def _pre_marker_file_content(self, pre_marker_file_content: str) -> None:
        self.__pre_marker_file_content = pre_marker_file_content


# fy:end <<<===
