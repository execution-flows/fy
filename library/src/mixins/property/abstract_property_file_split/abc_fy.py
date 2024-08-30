"""fy
property abstract_property_file_split: AbstractPropertyFileSplitModel
"""

import abc
from pydantic import BaseModel


class AbstractPropertyFileSplitModel(BaseModel):
    user_imports: str
    abstract_property_name: str
    property_type: str


# fy:start ===>>>
class AbstractPropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_property_file_split(self) -> AbstractPropertyFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
