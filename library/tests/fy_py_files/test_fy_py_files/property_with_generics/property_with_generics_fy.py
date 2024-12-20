# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import GreetingT


property hello_world[GreetingT]: str using spanish_greeting:
"""

from functools import cached_property
from typing import Generic
from .greetings_t import GreetingT


# fy:start ===>>>
class HelloWorld_UsingSpanishGreeting_PropertyMixin(
    Generic[GreetingT],
):
    @cached_property
    def _hello_world(self) -> str:
        # fy:end <<<===
        pass
