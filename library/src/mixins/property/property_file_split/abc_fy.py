"""fy
property property_file_split: PropertyFileSplit
"""

import abc
from pydantic import BaseModel


class PropertyFileSplitModel(BaseModel):
    user_imports: str
    property_name: str
    implementation_name: str
    property_type: str
    mixin_split: str


# fy:start ===>>>
class With_PropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _property_file_split(self) -> PropertyFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
