"""fy
property mixin_lines: str
"""

import abc


# fy:start ===>>>
class With_MixinLines_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _mixin_lines(self) -> str:
        raise NotImplementedError()
        # fy:end <<<===
