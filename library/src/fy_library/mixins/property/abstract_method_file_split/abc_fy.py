# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property abstract_method_file_split: AbstractMethodFileSplitModel
"""

import abc
from pydantic import BaseModel


class AbstractMethodFileSplitModel(BaseModel):
    user_imports: str
    abstract_method_name: str
    generics_def: str
    arguments: str | None
    return_type: str


# fy:start ===>>>
class AbstractMethodFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _abstract_method_file_split(self) -> AbstractMethodFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
