# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow FlowImports -> List[str]:
    property property_mixins using setter
    property parsed_fy_py_files_map_by_key using setter
    property property_setter_imports using property_mixins
    property user_imports_with_property_setter_imports using property_setter_imports
    property import_any using property_setters_exists
    property import_flow_base using constant
"""

from typing import List, Any, Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import PropertyMixinModel
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_mixins.using_setter import (
    PropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_setter_imports.using_property_mixin_fy import (
    PropertySetterImports_UsingPropertyMixins_PropertyMixin,
)
from fy_library.mixins.property.user_imports_with_property_setter_imports.using_property_setter_imports_fy import (
    UserImportsWithPropertySetterImports_UsingPropertySetterImports_PropertyMixin,
)

from fy_library.mixins.property.imports.import_any__using_property_setters_exists_fy import (
    ImportAny_UsingPropertySettersExists_PropertyMixin,
)

from fy_library.mixins.property.imports.import_flow_base__using_constant_fy import (
    ImportFlowBase_UsingConstant_PropertyMixin,
)


# fy:start ===>>>
class FlowImports_Flow(
    # Property Mixins
    PropertyMixins_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    PropertySetterImports_UsingPropertyMixins_PropertyMixin,
    UserImportsWithPropertySetterImports_UsingPropertySetterImports_PropertyMixin,
    ImportAny_UsingPropertySettersExists_PropertyMixin,
    ImportFlowBase_UsingConstant_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        property_mixins: List[PropertyMixinModel],
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        **kwargs: Any,
    ):
        self._property_mixins = property_mixins
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        return (
            self._user_imports_with_property_setter_imports
            + self._import_any
            + self._import_flow_base
        )
