import abc


class With_PostMarkerFileContent_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _post_marker_file_content(self) -> str:
        raise NotImplementedError()
