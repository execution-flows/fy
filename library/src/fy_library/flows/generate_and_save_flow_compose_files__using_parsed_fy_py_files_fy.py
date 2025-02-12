# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow generate_and_save_flow_compose_files__using_parsed_fy_py_files -> None:
    property mixin_import_map using setter
    property parsed_fy_py_files_map_by_key using setter
    property abstract_entities_ordering_index using setter
    property files_to_generate using setter
fy"""

from typing import Any

from fy_core.base.flow_base import FlowBase

from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.flows.generate_and_save_flow_compose_file__using_parsed_fy_py_file_fy import (
    GenerateAndSaveFlowComposeFile_UsingParsedFyPyFile_Flow,
)
from fy_library.mixins.property.imports_and_user_imports.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.mro.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.parsed_fy_py.files_to_generate.using_setter import (
    FilesToGenerate_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFlowComposeFiles_UsingParsedFyPyFiles_Flow(
    # Property Mixins
    MixinImportMap_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    FilesToGenerate_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        mixin_import_map: dict[tuple[ParsedFyPyFileKind, str], str],
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
        abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int],
        files_to_generate: list[ParsedFyPyFile],
        **kwargs: Any,
    ):
        self._mixin_import_map = mixin_import_map
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        self._files_to_generate = files_to_generate
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        for parsed_fy_py_file in self._files_to_generate:
            GenerateAndSaveFlowComposeFile_UsingParsedFyPyFile_Flow(
                parsed_fy_py_file=parsed_fy_py_file,
                mixin_import_map=self._mixin_import_map,
                parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
                abstract_entities_ordering_index=self._abstract_entities_ordering_index,
            )()
