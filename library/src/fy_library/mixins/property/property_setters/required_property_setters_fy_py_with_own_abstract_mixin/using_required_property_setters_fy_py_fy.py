# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import PropertySetterFyPyFile


property required_property_setters_fy_py_with_own_abstract_mixin: list[PropertySetterFyPyFile] using required_property_setters_fy_py:
    property required_property_setters_fy_py
    property parsed_fy_py_files_map_by_key
    property mixin_import_map
fy"""

import abc
from functools import cached_property
from typing import cast

from fy_library.domain.mixin_models import AbstractPropertyModel, MixinModelKind
from fy_library.domain.parsed_fy_py_file import (
    PropertySetterFyPyFile,
    ParsedAbstractPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.required_property_setters_fy_py.abc_fy import (
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.required_property_setters_fy_py_with_own_abstract_mixin.abc_fy import (
    RequiredPropertySettersFyPyWithOwnAbstractMixin_PropertyMixin_ABC,
)

from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.abc_fy import (
    MixinImportMap_PropertyMixin_ABC,
)


# fy:start ===>>>
class RequiredPropertySettersFyPyWithOwnAbstractMixin_UsingRequiredPropertySettersFyPy_PropertyMixin(
    # Property Mixins
    MixinImportMap_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    RequiredPropertySettersFyPy_PropertyMixin_ABC,
    RequiredPropertySettersFyPyWithOwnAbstractMixin_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_property_setters_fy_py_with_own_abstract_mixin(
        self,
    ) -> list[PropertySetterFyPyFile]:
        # fy:end <<<===
        def with_own_abstract_mixin(
            required_property_setter: PropertySetterFyPyFile,
        ) -> PropertySetterFyPyFile:
            match required_property_setter.file_type:
                case ParsedFyPyFileKind.PROPERTY_SETTER:
                    own_property_setter_entity_key = (
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        required_property_setter.property_name.snake_case,
                    )

                    parsed_abstract_property_fy_py_file = cast(
                        ParsedAbstractPropertyFyPyFile,
                        self._parsed_fy_py_files_map_by_key[
                            own_property_setter_entity_key
                        ],
                    )
                    return PropertySetterFyPyFile.model_validate(
                        {
                            **required_property_setter.model_dump(),
                            "abstract_property_import": self._mixin_import_map[
                                own_property_setter_entity_key
                            ],
                            "abstract_property_mixins": required_property_setter.abstract_property_mixins
                            + [
                                AbstractPropertyModel(
                                    python_class_name=parsed_abstract_property_fy_py_file.python_class_name,
                                    kind=MixinModelKind.ABSTRACT_PROPERTY,
                                    property_name=required_property_setter.property_name,
                                    generics_impl=(
                                        required_property_setter.generics_def
                                        or required_property_setter.property_type
                                    )
                                    if parsed_abstract_property_fy_py_file.generics_def
                                    != ""
                                    else "",
                                )
                            ],
                        }
                    )

        return [
            with_own_abstract_mixin(required_property_setter=required_property_setter)
            for required_property_setter in self._required_property_setters_fy_py
        ]
