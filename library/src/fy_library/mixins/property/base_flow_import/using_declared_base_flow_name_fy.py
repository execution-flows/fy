# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property base_flow_import: str using declared_base_flow_name:
    property parsed_fy_py_file
"""

import abc
from functools import cached_property

from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class BaseFlowImport_UsingDeclaredBaseFlowName_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _base_flow_import(self) -> str:
        # fy:end <<<===
        assert hasattr(self._parsed_fy_py_file, "declared_base_flow")

        return self._parsed_fy_py_file.declared_base_flow
