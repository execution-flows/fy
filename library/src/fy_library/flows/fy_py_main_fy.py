# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from pathlib import Path
from typing import Any


flow FyPy_Main -> None:
    property folder_to_parse using setter
    property project_root_folder using setter
    property fy_py_files_to_parse using files_discovery
    property parsed_fy_py_files using fy_py_parser
    property parsed_fy_py_files_map_by_key using parsed_fy_py_files
    property parsed_fy_py_files_with_own_abstract_mixin using parsed_fy_py_files_map_by_key
    property abstract_entities_ordering_index using parsed_fy_py_files_map_by_key
    property required_property_setters_fy_py using parsed_fy_py_files
    property mixin_import_map using parsed_fy_py_files
"""

from pathlib import Path
from typing import Any

from fy_core.base.flow_base import FlowBase

from fy_library.flows.generate_and_save_fy_py_files__using_parsed_fy_py_files_fy import (
    GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles_Flow,
)
from fy_library.flows.generate_and_save_fy_py_files__using_required_property_setters_fy import (
    GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow,
)
from fy_library.mixins.property.folder_to_parse.using_setter import (
    FolderToParse_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.fy_py_files_to_parse.using_files_discovery_fy import (
    FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin,
)
from fy_library.mixins.property.mixin_import_map.using_parsed_fy_py_files_fy import (
    MixinImportMap_UsingParsedFyPyFiles_PropertyMixin,
)
from fy_library.mixins.property.ordered_abstract_entities.using_parsed_fy_py_files_map_by_key_fy import (
    AbstractEntitiesOrderingIndex_UsingParsedFyPyFilesMapByKey_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files.using_fy_py_parser_fy import (
    ParsedFyPyFiles_UsingFyPyParser_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_parsed_fy_py_files_fy import (
    ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin,
)
from fy_library.mixins.property.project_root_folder.using_setter import (
    ProjectRootFolder_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.required_property_setters_fy_py.using_parsed_fy_py_files_fy import (
    RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin,
)

from fy_library.mixins.property.parsed_fy_py_files_with_own_abstract_mixin.using_parsed_fy_py_files_map_by_key_fy import (
    ParsedFyPyFilesWithOwnAbstractMixin_UsingParsedFyPyFilesMapByKey_PropertyMixin,
)


# fy:start ===>>>
class FyPy_Main_Flow(
    # Property Mixins
    FolderToParse_UsingSetter_PropertyMixin,
    ProjectRootFolder_UsingSetter_PropertyMixin,
    FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin,
    ParsedFyPyFiles_UsingFyPyParser_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin,
    ParsedFyPyFilesWithOwnAbstractMixin_UsingParsedFyPyFilesMapByKey_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingParsedFyPyFilesMapByKey_PropertyMixin,
    RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin,
    MixinImportMap_UsingParsedFyPyFiles_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        folder_to_parse: Path,
        project_root_folder: Path,
        **kwargs: Any,
    ):
        self._folder_to_parse = folder_to_parse
        self._project_root_folder = project_root_folder
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        # fy:end <<<===
        GenerateAndSaveFyPyFiles_UsingParsedFyPyFiles_Flow(
            parsed_fy_py_files=self._parsed_fy_py_files_with_own_abstract_mixin,
            mixin_import_map=self._mixin_import_map,
            parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
            abstract_entities_ordering_index=self._abstract_entities_ordering_index,
        )()
        GenerateAndSaveFyPyFiles_UsingRequiredPropertySetters_Flow(
            required_property_setters_fy_py=self._required_property_setters_fy_py,
        )()
