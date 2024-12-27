# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property abstract_entities_ordering_index: Dict[str, int] using parsed_fy_py_files_map_by_key:
    property parsed_fy_py_files_map_by_key
"""

from functools import cached_property

from typing import Dict

import abc

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)

from fy_library.mixins.property.ordered_abstract_entities.abc_fy import (
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
)


# fy:start ===>>>
class AbstractEntitiesOrderingIndex_UsingParsedFyPyFilesMapByKey_PropertyMixin(
    # Property_mixins
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_entities_ordering_index(self) -> Dict[str, int]:
        # fy:end <<<===
        abstract_entities_ordering_index = {
            entity_key: entity_num
            for entity_num, entity_key in enumerate(
                sorted(self._parsed_fy_py_files_map_by_key)
            )
            if self._parsed_fy_py_files_map_by_key[entity_key].file_type
            in {
                ParsedFyPyFileKind.ABSTRACT_METHOD,
                ParsedFyPyFileKind.ABSTRACT_PROPERTY,
            }
        }
        return abstract_entities_ordering_index
