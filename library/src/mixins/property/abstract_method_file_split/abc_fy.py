"""fy
property abstract_method_file_split: AbstractMethodFileSplitModel
"""

import abc
from pydantic import BaseModel


class AbstractMethodFileSplitModel(BaseModel):
    user_imports: str
    abstract_method_name: str
    arguments: str
    return_type: str


# fy:start ===>>>
class With_AbstractMethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_method_file_split(self) -> AbstractMethodFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
