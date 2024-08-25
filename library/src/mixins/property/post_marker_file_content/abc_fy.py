"""fy
property post_marker_file_content: str
"""

import abc


# fy:start <<<===
class With_PostMarkerFileContent_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _post_marker_file_content(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
