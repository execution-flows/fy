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
from typing import List, cast, Set

from fy_library.domain.fy_py_template_models import entity_key
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFileKind,
    ParsedMethodFyPyFile,
    ParsedFlowFyPyFile,
    ParsedPropertyFyPyFile,
)
from fy_library.flows.imports.abstract_method_imports_fy import (
    AbstractMethodImportsFlow_Flow,
)
from fy_library.flows.imports.abstract_property_imports_fy import (
    AbstractPropertyImportsFlow_Flow,
)
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


# fy:start ===>>>
class MixinImports_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    MixinImportMap_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_imports(self) -> List[str]:
        # fy:end <<<===
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                property_setters = [
                    property_mixin
                    for property_mixin in cast(
                        ParsedFlowFyPyFile, self._parsed_fy_py_file
                    ).template_model.properties
                    if property_mixin.implementation_name.snake_case == "setter"
                ]
                import_any = ["from typing import Any"] if property_setters else []
                user_imports: Set[str] = set()
                for property_setter in property_setters:
                    user_imports.update(
                        [
                            user_import
                            for user_import in self._parsed_fy_py_files_map_by_key[
                                property_setter.property_name.snake_case
                            ].user_imports.split("\n")
                            if user_import != ""
                        ]
                    )

                mixin_imports = (
                    import_any
                    + list(user_imports)
                    + [
                        # static imports
                        "from fy_core.base.flow_base import FlowBase",
                    ]
                    + [
                        # property mixins
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=property_mixin.property_name.snake_case,
                                mixin_implementation_name__snake_case=property_mixin.implementation_name.snake_case,
                            )
                        ]
                        for property_mixin in cast(
                            ParsedFlowFyPyFile, self._parsed_fy_py_file
                        ).template_model.properties
                    ]
                    + [
                        # method mixins
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=method_mixin.method_name.snake_case,
                                mixin_implementation_name__snake_case=method_mixin.implementation_name.snake_case,
                            )
                        ]
                        for method_mixin in cast(
                            ParsedFlowFyPyFile, self._parsed_fy_py_file
                        ).template_model.methods
                    ]
                )
                return mixin_imports
            case ParsedFyPyFileKind.METHOD:
                return MethodImports_Flow(
                    abstract_property_mixins=cast(
                        ParsedMethodFyPyFile, self._parsed_fy_py_file
                    ).template_model.abstract_property_mixins,
                    abstract_method_mixins=cast(
                        ParsedMethodFyPyFile, self._parsed_fy_py_file
                    ).template_model.abstract_method_mixins,
                    mixin_import_map=self._mixin_import_map,
                )()
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                return AbstractMethodImportsFlow_Flow()()
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                return AbstractPropertyImportsFlow_Flow()()
            case ParsedFyPyFileKind.PROPERTY:
                return PropertyImports_Flow(
                    abstract_property_mixins=cast(
                        ParsedPropertyFyPyFile, self._parsed_fy_py_file
                    ).template_model.abstract_property_mixins,
                    mixin_import_map=self._mixin_import_map,
                )()
            case _:
                raise NotImplementedError(
                    f"Mixin imports for {self._parsed_fy_py_file.file_type}"
                )
