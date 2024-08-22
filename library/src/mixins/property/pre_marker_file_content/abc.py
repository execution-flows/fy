import abc


class With_PreMarkerFileContent_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _pre_marker_file_content(self) -> str:
        raise NotImplementedError()
