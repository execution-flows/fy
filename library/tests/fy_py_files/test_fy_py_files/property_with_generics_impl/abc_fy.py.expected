# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from .greetings_t import SpanishGreetingT


property spanish_greeting: SpanishGreetingT
"""

import abc
from .greetings_t import SpanishGreetingT


# fy:start ===>>>
class SpanishGreeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _spanish_greeting(self) -> SpanishGreetingT:
        raise NotImplementedError()
        # fy:end <<<===
