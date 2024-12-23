# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles -> None:
    property parsed_fy_py_files using setter
    property mixin_import_map using setter
    property parsed_fy_py_files_map_by_key using setter
    property abstract_entities_ordering_index using setter
"""

from typing import List, Any, Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from fy_library.flows.generate_and_save_fy_py_file__using_parsed_fy_py_file_fy import (
    GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow,
)
from fy_library.mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files.using_setter import (
    ParsedFyPyFiles_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles_Flow(
    # Property Mixins
    ParsedFyPyFiles_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_files: List[ParsedFyPyFile],
        mixin_import_map: Dict[str, str],
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        abstract_entities_ordering_index: Dict[str, int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_files = parsed_fy_py_files
        self._mixin_import_map = mixin_import_map
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        for parsed_fy_py_file in self._parsed_fy_py_files:
            GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow(
                parsed_fy_py_file=parsed_fy_py_file,
                mixin_import_map=self._mixin_import_map,
                parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                abstract_entities_ordering_index=self._abstract_entities_ordering_index,
            )()
