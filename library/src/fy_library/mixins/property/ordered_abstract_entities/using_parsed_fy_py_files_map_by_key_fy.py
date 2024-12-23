# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import Dict


property ordered_abstract_entities: Dict[str, int] using parsed_fy_py_files_map_by_key:
    property parsed_fy_py_files_map_by_key
"""

from functools import cached_property

from typing import Dict

import abc

from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class OrderedAbstractEntities_UsingParsedFyPyFilesMapByKey_PropertyMixin(
    # Property_mixins
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _ordered_abstract_entities(self) -> Dict[str, int]:
        # fy:end <<<===
        ordered_abstract_entities = {
            entity_key: entity_num
            for entity_num, entity_key in enumerate(self._parsed_fy_py_files_map_by_key)
            if self._parsed_fy_py_files_map_by_key[entity_key].file_type
            in {
                ParsedFyPyFileKind.ABSTRACT_METHOD,
                ParsedFyPyFileKind.ABSTRACT_PROPERTY,
            }
        }
        return ordered_abstract_entities
