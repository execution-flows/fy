# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from ..greetings_t import FrenchGreeting


property french_greeting: FrenchGreeting
fy"""

import abc
from ..greetings_t import FrenchGreeting


# fy:start ===>>>
class FrenchGreeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _french_greeting(self) -> FrenchGreeting:
        raise NotImplementedError()
        # fy:end <<<===
