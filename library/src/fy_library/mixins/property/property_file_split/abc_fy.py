# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_file_split: PropertyFileSplitModel
"""

import abc
from pydantic import BaseModel


class PropertyFileSplitModel(BaseModel):
    user_imports: str
    property_name: str
    implementation_name: str
    generics_def: str
    property_type: str
    mixins: str


# fy:start ===>>>
class PropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _property_file_split(self) -> PropertyFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
