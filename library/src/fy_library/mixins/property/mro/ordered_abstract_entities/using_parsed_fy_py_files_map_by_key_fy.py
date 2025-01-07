# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int] using parsed_fy_py_files_map_by_key:
    property parsed_fy_py_files_map_by_key
fy"""

import abc
from functools import cached_property
from typing import cast

from fy_library.domain.parsed_fy_py_file import (
    ParsedAbstractPropertyFyPyFile,
    ParsedAbstractMethodFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.mro.ordered_abstract_entities.abc_fy import (
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class AbstractEntitiesOrderingIndex_UsingParsedFyPyFilesMapByKey_PropertyMixin(
    # Property Mixins
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_entities_ordering_index(
        self,
    ) -> dict[tuple[ParsedFyPyFileKind, str], int]:
        # fy:end <<<===
        def sorting_mixin_key(
            mixin_key: tuple[ParsedFyPyFileKind, str],
        ) -> tuple[int, tuple[ParsedFyPyFileKind, str]]:
            parsed_fy_py_file = self._parsed_fy_py_files_map_by_key[mixin_key]
            prefix_index: int
            match parsed_fy_py_file.file_type:
                case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                    abstract_property_parsed_fy_py_file = cast(
                        ParsedAbstractPropertyFyPyFile, parsed_fy_py_file
                    )
                    prefix_index = (
                        1
                        if len(abstract_property_parsed_fy_py_file.generics_def) > 0
                        else 0
                    )
                case ParsedFyPyFileKind.ABSTRACT_METHOD:
                    abstract_method_parsed_fy_py_file = cast(
                        ParsedAbstractMethodFyPyFile, parsed_fy_py_file
                    )
                    prefix_index = (
                        1
                        if len(abstract_method_parsed_fy_py_file.generics_def) > 0
                        else 0
                    )
                case _:
                    prefix_index = 0

            return prefix_index, mixin_key

        abstract_entities_ordering_index = {
            entity_key: entity_num
            for entity_num, entity_key in enumerate(
                sorted(self._parsed_fy_py_files_map_by_key, key=sorting_mixin_key)
            )
            if self._parsed_fy_py_files_map_by_key[entity_key].file_type
            in {
                ParsedFyPyFileKind.ABSTRACT_METHOD,
                ParsedFyPyFileKind.ABSTRACT_PROPERTY,
            }
        }
        return abstract_entities_ordering_index
