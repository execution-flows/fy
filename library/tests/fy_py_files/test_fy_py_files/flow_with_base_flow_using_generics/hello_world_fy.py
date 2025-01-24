# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import FrenchGreeting

flow hello_world(greeting[FrenchGreeting]) -> None:
fy"""

from fy_py_files.test_fy_py_files.flow_with_base_flow_using_generics.greeting_base_flow_fy import (
    Greeting_BaseFlow,
)
from .greetings_t import FrenchGreeting


# fy:start ===>>>
class HelloWorld_Flow(
    # Base
    Greeting_BaseFlow[FrenchGreeting],
):
    def __call__(self) -> None:
        # fy:end <<<===
        pass
