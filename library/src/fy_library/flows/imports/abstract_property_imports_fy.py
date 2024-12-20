# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow AbstractPropertyImportsFlow -> List[str]:
    property parsed_abstract_property_fy_py_file using setter
    property import_abc using constant
    property import_generic using generic_constant
"""

from typing import List, Any

from fy_core.base.flow_base import FlowBase

from fy_library.domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile
from fy_library.mixins.property.imports.import_abc__using_constant_fy import (
    ImportAbc_UsingConstant_PropertyMixin,
)
from fy_library.mixins.property.imports.import_generic__using_generic_constant_fy import (
    ImportGeneric_UsingGenericConstant_PropertyMixin,
)
from fy_library.mixins.property.parsed_abstract_property_fy_py_file.using_setter import (
    ParsedAbstractPropertyFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class AbstractPropertyImportsFlow_Flow(
    # Property Mixins
    ParsedAbstractPropertyFyPyFile_UsingSetter_PropertyMixin,
    ImportAbc_UsingConstant_PropertyMixin,
    ImportGeneric_UsingGenericConstant_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        parsed_abstract_property_fy_py_file: ParsedAbstractPropertyFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_abstract_property_fy_py_file = parsed_abstract_property_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        return (
            self._import_abc + self._import_generic
            if self._parsed_abstract_property_fy_py_file.generics_def != ""
            else self._import_abc
        )
