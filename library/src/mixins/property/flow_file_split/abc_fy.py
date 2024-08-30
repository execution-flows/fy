"""fy
property flow_file_split: FlowFileSplitModel
"""

import abc

from pydantic import BaseModel


class FlowFileSplitModel(BaseModel):
    user_imports: str
    flow_name: str
    return_type: str
    mixins: str


# fy:start ===>>>
class With_FlowFileSplit_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _flow_file_split(self) -> FlowFileSplitModel:
        raise NotImplementedError()
        # fy:end <<<===
