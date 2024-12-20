# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property abstract_property_file_split: AbstractPropertyFileSplitModel
"""

import abc

from pydantic import BaseModel


class AbstractPropertyFileSplitModel(BaseModel):
    user_imports: str
    abstract_property_name: str
    generics_def: str
    property_type: str


# fy:start ===>>>
class AbstractPropertyFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_property_file_split(self) -> AbstractPropertyFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
