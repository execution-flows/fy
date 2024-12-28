# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property hello: Message
fy"""

import abc

from pydantic import BaseModel


class Message(BaseModel):
    message: str


# fy:start ===>>>
class Hello_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _hello(self) -> Message:
        raise NotImplementedError()
        # fy:end <<<===
