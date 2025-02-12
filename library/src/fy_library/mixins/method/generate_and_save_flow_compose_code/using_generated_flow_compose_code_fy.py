# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method generate_and_save_flow_compose_code -> None using flow_compose_file_content:
    property flow_compose_file_content
    property flow_compose_file_name
fy"""

import abc

from fy_library.mixins.property.flow_compose_file.flow_compose_file_content.abc_fy import (
    FlowComposeFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.flow_compose_file.flow_compose_file_name.abc_fy import (
    FlowComposeFileName_PropertyMixin_ABC,
)


# fy:start ===>>>
class GenerateAndSaveFlowComposeCode_UsingFlowComposeFileContent_MethodMixin(
    # Property Mixins
    FlowComposeFileContent_PropertyMixin_ABC,
    FlowComposeFileName_PropertyMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_flow_compose_code(self) -> None:
        # fy:end <<<===
        flow_compose_file_content = self._flow_compose_file_content
        with open(
            file=self._flow_compose_file_name, mode="w", encoding="UTF-8"
        ) as setter_file:
            setter_file.write(flow_compose_file_content)
