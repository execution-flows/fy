# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
base flow HelloWorld(Greeting) -> None:
fy"""

import abc
from fy_py_files.test_fy_py_files.base_flow_with_base_flow.greeting_base_flow_fy import (
    Greeting_BaseFlow,
)


# fy:start ===>>>
class HelloWorld_BaseFlow(
    # Base
    Greeting_BaseFlow,
    abc.ABC,
):
    pass
    # fy:end <<<===
