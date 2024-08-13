# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from pathlib import Path
from typing import Any

from base.execution_flow_base import ExecutionFlowBase
from mixins.method.generate_py_files.using_jinja2_templates import GeneratePyFiles_UsingJinja2Templates_MethodMixin
from mixins.property.folder_to_parse.using_setter import FolderToParse_PropertyMixin
from mixins.property.fy_files_to_parse.using_files_discovery import \
    FyFilesToParse_UsingFilesDiscovery_PropertyMixin
from mixins.property.mixin_import_map.using_parsed_fy_files import MixinImportMap_UsingParsedFyFiles_PropertyMixin
from mixins.property.parsed_fy_files.using_fy_parser import ParsedFyFiles_UsingFyParser_PropertyMixin


class Main_Flow(
    # Properties
    FolderToParse_PropertyMixin,
    FyFilesToParse_UsingFilesDiscovery_PropertyMixin,
    ParsedFyFiles_UsingFyParser_PropertyMixin,
    MixinImportMap_UsingParsedFyFiles_PropertyMixin,
    # Methods
    GeneratePyFiles_UsingJinja2Templates_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __init__(
        self,
        *args: Any,
        folder_to_parse: Path,
        **kwargs: Any,
    ):
        self._folder_to_parse = folder_to_parse
        super().__init__(*args, **kwargs)

    def __call__(self) -> None:
        self._generate_py_files()
