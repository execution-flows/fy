# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property base_flow_file_split: BaseFlowFileSplitModel
"""

import abc

from pydantic import BaseModel


class BaseFlowFileSplitModel(BaseModel):
    user_imports: str
    base_flow_name: str
    return_type: str
    mixins: str


# fy:start ===>>>
class BaseFlowFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _base_flow_file_split(self) -> BaseFlowFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
