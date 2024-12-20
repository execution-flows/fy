# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT


method greet[GreetingT](greeting: str) -> int using constant:
"""

from typing import Generic
from .greetings_t import GreetingT


# fy:start ===>>>
class Greet_UsingConstant_MethodMixin(
    Generic[GreetingT],
):
    def _greet(self, greeting: str) -> int:
        # fy:end <<<===
        pass
