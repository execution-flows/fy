# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List


property mixin_imports: List[str] using parsed_fy_py_file:
    property parsed_fy_py_file
    property mixin_import_map
    property parsed_fy_py_files_map_by_key
"""

import abc
from functools import cached_property
from typing import List, cast

from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFileKind,
    ParsedMethodFyPyFile,
    ParsedFlowFyPyFile,
    ParsedPropertyFyPyFile,
    ParsedBaseFlowFyPyFile,
    ParsedAbstractPropertyFyPyFile,
    ParsedAbstractMethodFyPyFile,
)
from fy_library.flows.imports.abstract_method_imports_fy import (
    AbstractMethodImportsFlow_Flow,
)
from fy_library.flows.imports.abstract_property_imports_fy import (
    AbstractPropertyImportsFlow_Flow,
)
from fy_library.flows.imports.base_flow_imports_fy import BaseFlowImports_Flow
from fy_library.flows.imports.flow_imports_fy import FlowImports_Flow
from fy_library.flows.imports.method_imports_fy import MethodImports_Flow
from fy_library.flows.imports.property_imports_fy import PropertyImports_Flow
from fy_library.mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)

from fy_library.mixins.property.mixin_imports.abc_fy import (
    MixinImports_PropertyMixin_ABC,
)


# fy:start ===>>>
class MixinImports_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    MixinImportMap_PropertyMixin_ABC,
    MixinImports_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_imports(self) -> List[str]:
        # fy:end <<<===
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                parsed_flow_fy_py_file = cast(
                    ParsedFlowFyPyFile, self._parsed_fy_py_file
                )
                return FlowImports_Flow(
                    property_mixins=parsed_flow_fy_py_file.properties,
                    parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                    mixin_import_map=self._mixin_import_map,
                    method_mixins=cast(
                        ParsedFlowFyPyFile, self._parsed_fy_py_file
                    ).methods,
                    parsed_flow_fy_py_file=parsed_flow_fy_py_file,
                )()
            case ParsedFyPyFileKind.BASE_FLOW:
                parsed_base_flow_fy_py_file = cast(
                    ParsedBaseFlowFyPyFile, self._parsed_fy_py_file
                )
                return BaseFlowImports_Flow(
                    property_mixins=parsed_base_flow_fy_py_file.properties,
                    parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                    mixin_import_map=self._mixin_import_map,
                    method_mixins=parsed_base_flow_fy_py_file.methods,
                    abstract_property_mixins=parsed_base_flow_fy_py_file.abstract_property_mixins,
                    abstract_method_mixins=parsed_base_flow_fy_py_file.abstract_method_mixins,
                    parsed_base_flow_fy_py_file=parsed_base_flow_fy_py_file,
                )()
            case ParsedFyPyFileKind.METHOD:
                parsed_method_fy_py_file = cast(
                    ParsedMethodFyPyFile, self._parsed_fy_py_file
                )
                return MethodImports_Flow(
                    abstract_property_mixins=parsed_method_fy_py_file.abstract_property_mixins,
                    abstract_method_mixins=parsed_method_fy_py_file.abstract_method_mixins,
                    mixin_import_map=self._mixin_import_map,
                    parsed_method_fy_py_file=parsed_method_fy_py_file,
                )()
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                return AbstractMethodImportsFlow_Flow(
                    parsed_abstract_method_fy_py_file=cast(
                        ParsedAbstractMethodFyPyFile, self._parsed_fy_py_file
                    ),
                )()
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                return AbstractPropertyImportsFlow_Flow(
                    parsed_abstract_property_fy_py_file=cast(
                        ParsedAbstractPropertyFyPyFile, self._parsed_fy_py_file
                    ),
                )()
            case ParsedFyPyFileKind.PROPERTY:
                parsed_property_fy_py_file = cast(
                    ParsedPropertyFyPyFile, self._parsed_fy_py_file
                )
                return PropertyImports_Flow(
                    abstract_property_mixins=parsed_property_fy_py_file.abstract_property_mixins,
                    mixin_import_map=self._mixin_import_map,
                    parsed_property_fy_py_file=parsed_property_fy_py_file,
                )()
            case _:
                raise NotImplementedError(
                    f"Mixin imports for {self._parsed_fy_py_file.file_type}"
                )
