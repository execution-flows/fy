# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow FlowImports -> List[str]:
    property property_mixins using setter
    property method_mixins using setter
    property parsed_fy_py_files_map_by_key using setter
    property mixin_import_map using setter
    property property_setter_mixins using property_mixins
    property user_imports_from_mixins using property_setter_mixins
    property import_any using property_setters_exists
    property import_flow_base using constant
    property property_mixins_import using property_mixins_and_mixin_import_map
    property method_mixins_import using method_mixins_and_mixin_import_map

"""

from typing import List, Any, Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.mixin_models import MethodMixinModel, PropertyMixinModel
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.imports.import_any__using_property_setters_exists_fy import (
    ImportAny_UsingPropertySettersExists_PropertyMixin,
)
from fy_library.mixins.property.imports.import_flow_base__using_constant_fy import (
    ImportFlowBase_UsingConstant_PropertyMixin,
)
from fy_library.mixins.property.imports.property_mixins_imports__using_property_mixins_and_mixin_import_map_fy import (
    PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.method_mixins.using_setter import (
    MethodMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_mixins.using_setter import (
    PropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_setter_mixins.using_property_mixin_fy import (
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
)

from fy_library.mixins.property.imports.method_mixins_imports__using_method_mixins_and_mixin_import_map_fy import (
    MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin,
)

from fy_library.mixins.property.user_imports_from_property_mixins.using_property_setter_imports_fy import (
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
)


# fy:start ===>>>
class FlowImports_Flow(
    # Property Mixins
    PropertyMixins_UsingSetter_PropertyMixin,
    MethodMixins_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
    ImportAny_UsingPropertySettersExists_PropertyMixin,
    ImportFlowBase_UsingConstant_PropertyMixin,
    PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin,
    MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        property_mixins: List[PropertyMixinModel],
        method_mixins: List[MethodMixinModel],
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        mixin_import_map: Dict[str, str],
        **kwargs: Any,
    ):
        self._property_mixins = property_mixins
        self._method_mixins = method_mixins
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._mixin_import_map = mixin_import_map
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        return (
            self._user_imports_from_mixins
            + self._import_any
            + self._import_flow_base
            + self._property_mixins_import
            + self._method_mixins_import
        )
