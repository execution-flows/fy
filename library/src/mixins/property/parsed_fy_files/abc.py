# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
from typing import List

from domain.parsed_fy_file import ParsedFyFile


class With_ParsedFyFiles_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parsed_fy_files(self) -> List[ParsedFyFile]:
        raise NotImplementedError()
