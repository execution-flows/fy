# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import Greet


method greet[Greet](message: str) -> str using greeting:
"""

from typing import Generic
from ..greetings_t import Greet


# fy:start ===>>>
class Greet_UsingGreeting_MethodMixin(
    Generic[Greet],
):
    def _greet(self, message: str) -> str:
        # fy:end <<<===
        return message
