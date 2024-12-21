# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetT


method greet[GreetT](message: str) -> str using greeting_message:
"""

from typing import Generic
from ..greetings_t import GreetT


# fy:start ===>>>
class Greet_UsingGreetingMessage_MethodMixin(
    Generic[GreetT],
):
    def _greet(self, message: str) -> str:
        # fy:end <<<===
        return ""
