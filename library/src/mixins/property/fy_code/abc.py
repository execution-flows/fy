import abc


class With_FyCode_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _fy_code(self) -> str:
        raise NotImplementedError()
