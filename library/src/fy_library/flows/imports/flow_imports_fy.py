# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow flow_imports -> List[str]:
    property property_mixins using setter
    property method_mixins using setter
    property parsed_fy_py_files_map_by_key using setter
    property mixin_import_map using setter
    property parsed_flow_fy_py_file using setter
    property import_generic using constant(["from typing import Generic"])
    property declared_base_flow_name using parsed_flow_fy_py_file
    property property_setter_mixins using property_mixins
    property property_constant_setter_mixins using property_mixins
    property user_imports_from_mixins using property_setter_mixins
    property import_any using property_setters_exists
    property import_flow_base using constant(["from fy_core.base.flow_base import FlowBase"])
    property import_base_flow using declared_base_flow_name
    property property_mixins_import using property_mixins_and_mixin_import_map
    property method_mixins_import using method_mixins_and_mixin_import_map
fy"""

from typing import List, Any

from fy_core.base.flow_base import FlowBase

from fy_library.domain.mixin_models import MethodMixinModel, PropertyMixinModel
from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.entity_mixins.method_mixins.using_setter import (
    MethodMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.entity_mixins.property_mixins.using_setter import (
    PropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.import_flow_base.using_setter import (
    ImportFlowBase_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.import_generic.using_setter import (
    ImportGeneric_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.import_any__using_property_setters_exists_fy import (
    ImportAny_UsingPropertySettersExists_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.import_base_flow__using_declared_base_flow_name_fy import (
    ImportBaseFlow_UsingDeclaredBaseFlowName_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.method_mixins_imports__using_method_mixins_and_mixin_import_map_fy import (
    MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.imports.property_mixins_imports__using_property_mixins_and_mixin_import_map_fy import (
    PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports_and_user_imports.user_imports_from_property_mixins.using_property_setter_imports_fy import (
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.declared_base_flow_name.using_parsed_flow_fy_py_file_fy import (
    DeclaredBaseFlowName_UsingParsedFlowFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.parsed_entity_fy_py_file.parsed_flow_fy_py_file.using_setter import (
    ParsedFlowFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_setters.property_constant_setter_mixins.using_property_mixins_fy import (
    PropertyConstantSetterMixins_UsingPropertyMixins_PropertyMixin,
)
from fy_library.mixins.property.property_setters.property_setter_mixins.using_property_mixin_fy import (
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
)


# fy:start ===>>>
class FlowImports_Flow(
    # Property Mixins
    PropertyMixins_UsingSetter_PropertyMixin,
    MethodMixins_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedFlowFyPyFile_UsingSetter_PropertyMixin,
    ImportGeneric_UsingSetter_PropertyMixin,
    DeclaredBaseFlowName_UsingParsedFlowFyPyFile_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    PropertyConstantSetterMixins_UsingPropertyMixins_PropertyMixin,
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
    ImportAny_UsingPropertySettersExists_PropertyMixin,
    ImportFlowBase_UsingSetter_PropertyMixin,
    ImportBaseFlow_UsingDeclaredBaseFlowName_PropertyMixin,
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
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
        mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str],
        parsed_flow_fy_py_file: ParsedFlowFyPyFile,
        **kwargs: Any,
    ):
        self._property_mixins = property_mixins
        self._method_mixins = method_mixins
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._mixin_import_map = mixin_import_map
        self._parsed_flow_fy_py_file = parsed_flow_fy_py_file
        self._import_generic = ["from typing import Generic"]
        self._import_flow_base = ["from fy_core.base.flow_base import FlowBase"]
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        base_flow_import = (
            self._import_flow_base
            if self._import_base_flow == []
            else self._import_base_flow
        )

        generic_import = (
            self._import_generic
            if self._parsed_flow_fy_py_file.generics_def != ""
            else []
        )

        return (
            self._user_imports_from_mixins
            + self._import_any
            + base_flow_import
            + generic_import
            + self._property_mixins_import
            + self._method_mixins_import
        )
