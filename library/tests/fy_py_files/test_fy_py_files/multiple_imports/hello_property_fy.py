# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_py_files.test_fy_py_files.multiple_imports.abc_fy import Message


property hello: Message using domain:
fy"""

from functools import cached_property
import abc

from fy_py_files.test_fy_py_files.multiple_imports.abc_fy import Message

from fy_py_files.test_fy_py_files.multiple_imports.abc_fy import Hello_PropertyMixin_ABC


# fy:start ===>>>
class Hello_UsingDomain_PropertyMixin(
    # Property_mixins
    Hello_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _hello(self) -> Message:
        # fy:end <<<===
        return Message(
            message="Hello World!",
        )
