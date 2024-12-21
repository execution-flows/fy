# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import FrenchGreeting


property greeting: FrenchGreeting using greeting_message:
"""

from functools import cached_property
from ..greetings_t import FrenchGreeting


# fy:start ===>>>
class Greeting_UsingGreetingMessage_PropertyMixin:
    @cached_property
    def _greeting(self) -> FrenchGreeting:
        # fy:end <<<===
        return FrenchGreeting()
