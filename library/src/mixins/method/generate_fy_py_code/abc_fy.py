# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


method generate_fy_py_code(jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile) -> str
"""

import abc
from domain.parsed_fy_py_file import ParsedFyPyFile


# fy:start ===>>>
class GenerateFyPyCode_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _generate_fy_py_code(
        self, jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
    ) -> str:
        raise NotImplementedError()
        # fy:end <<<===
