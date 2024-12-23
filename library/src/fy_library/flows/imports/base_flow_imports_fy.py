# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


flow BaseFlowImports -> List[str]:
    property property_mixins using setter
    property method_mixins using setter
    property abstract_property_mixins using setter
    property abstract_method_mixins using setter
    property parsed_fy_py_files_map_by_key using setter
    property mixin_import_map using setter
    property parsed_base_flow_fy_py_file using setter
    property import_generic using generic_constant
    property declared_base_flow_name using parsed_base_flow_fy_py_file
    property property_setter_mixins using property_mixins
    property user_imports_from_mixins using property_setter_mixins
    property import_abc using constant
    property import_any using property_setters_exists
    property import_flow_base using constant
    property import_base_flow using declared_base_flow_name
    property property_mixins_import using property_mixins_and_mixin_import_map
    property method_mixins_import using method_mixins_and_mixin_import_map
    property import_abstract_property_mixins using abstract_property_mixin_and_mixin_import_map
    property import_abstract_method_mixins using abstract_method_mixin_and_mixin_import_map
"""

from typing import List, Any, Dict

from fy_core.base.flow_base import FlowBase

from fy_library.domain.mixin_models import (
    MethodMixinModel,
    AbstractMethodModel,
    AbstractPropertyModel,
    PropertyMixinModel,
)
from fy_library.domain.parsed_fy_py_file import ParsedBaseFlowFyPyFile
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile
from fy_library.mixins.property.abstract_method_mixins.using_setter import (
    AbstractMethodMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.abstract_property_mixins.using_setter import (
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.imports.import__abstract_property_mixins__using_abstract_property_mixin_and_mixin_import_map__fy import (
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports.import_abc__using_constant_fy import (
    ImportAbc_UsingConstant_PropertyMixin,
)
from fy_library.mixins.property.imports.import_abstract_method_mixins__using_abstract_method_mixin_and_mixin_import_map__fy import (
    ImportAbstractMethodMixins_UsingAbstractMethodMixinAndMixinImportMap_PropertyMixin,
)
from fy_library.mixins.property.imports.import_any__using_property_setters_exists_fy import (
    ImportAny_UsingPropertySettersExists_PropertyMixin,
)
from fy_library.mixins.property.imports.import_base_flow__using_declared_base_flow_name_fy import (
    ImportBaseFlow_UsingDeclaredBaseFlowName_PropertyMixin,
)
from fy_library.mixins.property.imports.import_flow_base__using_constant_fy import (
    ImportFlowBase_UsingConstant_PropertyMixin,
)
from fy_library.mixins.property.imports.method_mixins_imports__using_method_mixins_and_mixin_import_map_fy import (
    MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin,
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
from fy_library.mixins.property.user_imports_from_property_mixins.using_property_setter_imports_fy import (
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
)

from fy_library.mixins.property.parsed_base_flow_fy_py_file.using_setter import (
    ParsedBaseFlowFyPyFile_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.declared_base_flow_name.using_parsed_base_flow_fy_py_file_fy import (
    DeclaredBaseFlowName_UsingParsedBaseFlowFyPyFile_PropertyMixin,
)

from fy_library.mixins.property.imports.import_generic__using_generic_constant_fy import (
    ImportGeneric_UsingGenericConstant_PropertyMixin,
)


# fy:start ===>>>
class BaseFlowImports_Flow(
    # Property Mixins
    PropertyMixins_UsingSetter_PropertyMixin,
    MethodMixins_UsingSetter_PropertyMixin,
    AbstractPropertyMixins_UsingSetter_PropertyMixin,
    AbstractMethodMixins_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedBaseFlowFyPyFile_UsingSetter_PropertyMixin,
    ImportGeneric_UsingGenericConstant_PropertyMixin,
    DeclaredBaseFlowName_UsingParsedBaseFlowFyPyFile_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    UserImportsFromMixins_UsingPropertySetterMixins_PropertyMixin,
    ImportAbc_UsingConstant_PropertyMixin,
    ImportAny_UsingPropertySettersExists_PropertyMixin,
    ImportFlowBase_UsingConstant_PropertyMixin,
    ImportBaseFlow_UsingDeclaredBaseFlowName_PropertyMixin,
    PropertyMixinsImport_UsingPropertyMixinsAndMixinImportMap_PropertyMixin,
    MethodMixinsImport_UsingMethodMixinsAndMixinImportMap_PropertyMixin,
    ImportAbstractPropertyMixins_UsingAbstractPropertyMixinAndMixinImportMap_PropertyMixin,
    ImportAbstractMethodMixins_UsingAbstractMethodMixinAndMixinImportMap_PropertyMixin,
    # Base
    FlowBase[List[str]],
):
    def __init__(
        self,
        *args: Any,
        property_mixins: List[PropertyMixinModel],
        method_mixins: List[MethodMixinModel],
        abstract_property_mixins: List[AbstractPropertyModel],
        abstract_method_mixins: List[AbstractMethodModel],
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        mixin_import_map: Dict[str, str],
        parsed_base_flow_fy_py_file: ParsedBaseFlowFyPyFile,
        **kwargs: Any,
    ):
        self._property_mixins = property_mixins
        self._method_mixins = method_mixins
        self._abstract_property_mixins = abstract_property_mixins
        self._abstract_method_mixins = abstract_method_mixins
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._mixin_import_map = mixin_import_map
        self._parsed_base_flow_fy_py_file = parsed_base_flow_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> List[str]:
        # fy:end <<<===
        base_flow_import = (
            self._import_flow_base
            if self._import_base_flow == []
            else self._import_base_flow
        )

        import_generic_constant = (
            self._import_generic
            if self._parsed_base_flow_fy_py_file.generics_def != ""
            else []
        )

        return (
            self._user_imports_from_mixins
            + self._import_any
            + self._import_abc
            + import_generic_constant
            + base_flow_import
            + self._property_mixins_import
            + self._method_mixins_import
            + self._import_abstract_property_mixins
            + self._import_abstract_method_mixins
        )
