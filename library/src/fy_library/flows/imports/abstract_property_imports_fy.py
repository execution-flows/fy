# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow abstract_property_imports_flow -> List[str]:
    property parsed_abstract_property_fy_py_file using setter
    property import_abc using constant(["import abc"])
    property import_generic using constant(["from typing import Generic"])
fy"""

from typing import List, Any

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile
from fy_library.mixins.property.imports_and_user_imports.import_abc.using_setter import (
    ImportAbc_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.import_generic.using_setter import (
    ImportGeneric_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_abstract_property_fy_py_file.using_setter import (
    ParsedAbstractPropertyFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class AbstractPropertyImportsFlow_Flow(
    # Property Mixins
    ParsedAbstractPropertyFyPyFile_UsingSetter_PropertyMixin,
    ImportAbc_UsingSetter_PropertyMixin,
    ImportGeneric_UsingSetter_PropertyMixin,
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
        self._import_abc = ["import abc"]
        self._import_generic = ["from typing import Generic"]
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        return (
            self._import_abc + self._import_generic
            if self._parsed_abstract_property_fy_py_file.generics_def != ""
            else self._import_abc
        )
