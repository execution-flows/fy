# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property method_file_split: MethodFileSplitModel
"""

import abc

from pydantic import BaseModel


class MethodFileSplitModel(BaseModel):
    user_imports: str
    method_name: str
    generics_def: str
    arguments: str | None
    return_type: str
    implementation_name: str
    mixins: str


# fy:start ===>>>
class MethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _method_file_split(self) -> MethodFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
