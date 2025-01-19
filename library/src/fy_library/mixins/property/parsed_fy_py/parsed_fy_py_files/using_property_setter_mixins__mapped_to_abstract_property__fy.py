# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files: List[ParsedFyPyFile] using property_setter_mixins__mapped_to_abstract_property:
    property property_setter_mixins
    property parsed_fy_py_files_map_by_key
fy"""

import abc
from functools import cached_property
from typing import List, cast

from fy_library.domain.mixin_models import PropertyMixinModel
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedAbstractPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.abc_fy import (
    ParsedFyPyFiles_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_setters.property_setter_mixins.abc_fy import (
    PropertySetterMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin(
    # Property Mixins
    ParsedFyPyFiles_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    PropertySetterMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        def replace_generics_impl_type(
            parsed_abstract_property: ParsedAbstractPropertyFyPyFile,
            property_mixin: PropertyMixinModel,
        ) -> ParsedAbstractPropertyFyPyFile:
            if property_mixin.generics_impl == "":
                return parsed_abstract_property
            return ParsedAbstractPropertyFyPyFile(
                **parsed_abstract_property.model_dump(exclude={"property_type"}),
                property_type=property_mixin.generics_impl,
            )

        return [
            replace_generics_impl_type(
                parsed_abstract_property=cast(
                    ParsedAbstractPropertyFyPyFile,
                    self._parsed_fy_py_files_map_by_key[
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        property_setter.property_name.snake_case,
                    ],
                ),
                property_mixin=property_setter,
            )
            for property_setter in self._property_setter_mixins
        ]
