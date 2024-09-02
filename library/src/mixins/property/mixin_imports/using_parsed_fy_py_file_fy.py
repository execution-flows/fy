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

from domain.fy_py_template_models import entity_key
from domain.parsed_fy_py_file import (
    ParsedFyPyFileKind,
    ParsedMethodFyPyFile,
    ParsedFlowFyPyFile,
    ParsedPropertyFyPyFile,
)
from mixins.property.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
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
                        "from fy_core import FlowBase",
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
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                        or cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_method_mixins
                    )
                    else []
                )
                mixin_imports = (
                    static_imports
                    + [
                        # property mixins
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                    + [
                        # method mixins
                        self._mixin_import_map[
                            abstract_method_mixin.method_name.snake_case
                        ]
                        for abstract_method_mixin in cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_method_mixins
                    ]
                )
                return mixin_imports
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                return ["import abc"]
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                return ["import abc"]
            case ParsedFyPyFileKind.PROPERTY:
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedPropertyFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    )
                    else []
                )
                cached_import = ["from functools import cached_property"]
                mixin_imports = (
                    cached_import
                    + static_imports
                    + [
                        # property mixins
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedPropertyFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                )
                return mixin_imports
            case _:
                raise NotImplementedError(
                    f"Mixin imports for {self._parsed_fy_py_file.file_type}"
                )
