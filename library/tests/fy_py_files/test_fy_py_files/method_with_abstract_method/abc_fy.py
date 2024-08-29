"""fy
method encrypt(message: str) -> datetime.datetime
"""

import abc

import datetime


# fy:start ===>>>
class With_Encrypt_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _encrypt(self, message: str) -> datetime.datetime:
        raise NotImplementedError()
        # fy:end <<<===
