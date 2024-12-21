# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property flow_file_split: FlowFileSplitModel
"""

import abc

from pydantic import BaseModel


class FlowFileSplitModel(BaseModel):
    user_imports: str
    flow_name: str
    generics_def: str
    declared_base_flow: str
    return_type: str
    mixins: str


# fy:start ===>>>
class FlowFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _flow_file_split(self) -> FlowFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
