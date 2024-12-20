# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .method_greeting_t import MethodGreetingT


method greet[MethodGreetingT](greeting: str)
"""

import abc
from typing import Generic
from .method_greeting_t import MethodGreetingT


# fy:start ===>>>
class Greet_MethodMixin_ABC(
    Generic[MethodGreetingT],
    abc.ABC,
):
    @abc.abstractmethod
    def _greet(self, greeting: str) -> MethodGreetingT:
        raise NotImplementedError()
        # fy:end <<<===
