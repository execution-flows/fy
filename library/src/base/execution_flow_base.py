# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
from typing import Generic, TypeVar

ResultT = TypeVar("ResultT")


class ExecutionFlowBase(Generic[ResultT], abc.ABC):
    @abc.abstractmethod
    def __call__(self) -> ResultT:
        raise NotImplementedError()
