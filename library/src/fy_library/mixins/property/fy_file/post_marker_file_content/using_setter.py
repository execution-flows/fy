# fy:start ===>>>
from fy_library.mixins.property.fy_file.post_marker_file_content.abc_fy import (
    PostMarkerFileContent_PropertyMixin_ABC,
)


class PostMarkerFileContent_UsingSetter_PropertyMixin(
    PostMarkerFileContent_PropertyMixin_ABC,
):
    @property
    def _post_marker_file_content(self) -> str:
        return self.__post_marker_file_content

    @_post_marker_file_content.setter
    def _post_marker_file_content(self, post_marker_file_content: str) -> None:
        self.__post_marker_file_content = post_marker_file_content


# fy:end <<<===
