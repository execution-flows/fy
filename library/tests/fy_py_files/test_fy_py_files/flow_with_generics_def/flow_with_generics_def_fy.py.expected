# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT


flow HelloWorld[GreetingT] -> None:
"""

from fy_core.base.flow_base import FlowBase
from typing import Generic
from .greetings_t import GreetingT


# fy:start ===>>>
class HelloWorld_Flow(
    # Base
    FlowBase[None],
    Generic[GreetingT],
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
