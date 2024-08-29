"""fy
property method_file_split: MethodFileSplitModel
"""

from typing import List
import abc

from pydantic import BaseModel


class MethodFileSplitModel(BaseModel):
    user_imports: str
    method_name: str
    implementation_name: str
    arguments: str | None
    return_type: str
    mixin_split: List[str]


# fy:start ===>>>
class With_MethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_file_split(self) -> MethodFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
