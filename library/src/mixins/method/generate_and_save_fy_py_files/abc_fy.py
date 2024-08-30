# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
method generate_and_save_fy_py_files -> None
"""

import abc


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _generate_and_save_fy_py_files(self) -> None:
        raise NotImplementedError()
        # fy:end <<<===
