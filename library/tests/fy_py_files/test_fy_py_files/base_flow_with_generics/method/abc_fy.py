# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import GreetT


method greet[GreetT](message: str) -> GreetT
fy"""

import abc
from typing import Generic
from ..greetings_t import GreetT


# fy:start ===>>>
class Greet_MethodMixin_ABC(
    Generic[GreetT],
    abc.ABC,
):
    @abc.abstractmethod
    def _greet(self, message: str) -> GreetT:
        raise NotImplementedError()
        # fy:end <<<===
