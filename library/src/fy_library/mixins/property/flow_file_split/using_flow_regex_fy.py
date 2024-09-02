# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property flow_file_split: FlowFileSplitModel using flow_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
)
from fy_library.mixins.property.flow_file_split.abc_fy import FlowFileSplitModel
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class FlowFileSplit_UsingFlowRegex_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _flow_file_split(self) -> FlowFileSplitModel:
        # fy:end <<<===
        flow_string_split_regex = re.compile(
            rf"flow\s+(?P<flow_name>{FY_ENTITY_REGEX_STRING})\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING}):\s*\n"
        )

        flow_file_split = flow_string_split_regex.split(self._fy_code)

        assert (
            len(flow_file_split)
        ) == 4, f"Flow file split length {len(flow_file_split)} is invalid."

        flow_file_split_model = FlowFileSplitModel(
            user_imports=flow_file_split[0],
            flow_name=flow_file_split[1],
            return_type=flow_file_split[2],
            mixins=flow_file_split[3],
        )

        return flow_file_split_model
