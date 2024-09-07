# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property base_flow_file_split: BaseFlowFileSplitModel using base_flow_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
)
from fy_library.mixins.property.base_flow_file_split.abc_fy import (
    BaseFlowFileSplitModel,
)
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)

_BASE_FLOW_STRING_SPLIT_REGEX = re.compile(
    rf"base\s+flow\s+(?P<base_flow_name>{FY_ENTITY_REGEX_STRING})\s+->"
    rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING}):\s*\n"
)


# fy:start ===>>>
class BaseFlowFileSplit_UsingBaseFlowRegex_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _base_flow_file_split(self) -> BaseFlowFileSplitModel:
        # fy:end <<<===
        base_flow_file_split = _BASE_FLOW_STRING_SPLIT_REGEX.split(self._fy_code)

        assert (
            len(base_flow_file_split)
        ) == 4, f"Flow file split length {len(base_flow_file_split)} is invalid."

        base_flow_file_split_model = BaseFlowFileSplitModel(
            user_imports=base_flow_file_split[0],
            base_flow_name=base_flow_file_split[1],
            return_type=base_flow_file_split[2],
            mixins=base_flow_file_split[3],
        )

        return base_flow_file_split_model
