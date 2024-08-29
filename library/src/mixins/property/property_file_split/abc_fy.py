"""fy
property property_file_split: PropertyFileSplit
"""

import abc
from typing import List

from pydantic import BaseModel

from domain.python_entity_name import PythonEntityName


class PropertyFileSplitModel(BaseModel):
    user_imports: str
    python_class_name: PythonEntityName
    property_name: PythonEntityName
    implementation_name: PythonEntityName
    property_type: str
    mixin_split: List[str]


# fy:start ===>>>
class With_PropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _property_file_split(self) -> PropertyFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
