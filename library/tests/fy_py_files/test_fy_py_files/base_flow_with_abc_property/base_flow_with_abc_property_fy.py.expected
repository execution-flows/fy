# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
base flow WithAbcProperty -> None:
    property greeting
"""

import abc
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.base_flow_with_abc_property.abc_fy import (
    Greeting_PropertyMixin_ABC,
)


# fy:start ===>>>
class WithAbcProperty_BaseFlow(
    # Abstract Property Mixins
    Greeting_PropertyMixin_ABC,
    # Base
    FlowBase[None],
    abc.ABC,
):
    pass
    # fy:end <<<===
