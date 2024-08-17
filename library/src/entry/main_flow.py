from base.execution_flow_base import ExecutionFlowBase

from mixins.property.folder_to_parse.using_setter import (
    FolderToParse_UsingSetter_PropertyMixin,
)
from mixins.property.project_root_folder.using_setter import (
    ProjectRootFolder_UsingSetter_PropertyMixin,
)
from mixins.property.fy_files_to_parse.using_files_discovery import (
    FyFilesToParse_UsingFilesDiscovery_PropertyMixin,
)
from mixins.property.parsed_fy_files.using_fy_parser import (
    ParsedFyFiles_UsingFyParser_PropertyMixin,
)
from mixins.property.mixin_import_map.using_parsed_fy_files import (
    MixinImportMap_UsingParsedFyFiles_PropertyMixin,
)
from mixins.method.generate_py_files.using_jinja2_templates import (
    GeneratePyFiles_UsingJinja2Templates_MethodMixin,
)
from pathlib import Path
from typing import Any


class Main_Flow(
    # Property Mixins
    FolderToParse_UsingSetter_PropertyMixin,
    ProjectRootFolder_UsingSetter_PropertyMixin,
    FyFilesToParse_UsingFilesDiscovery_PropertyMixin,
    ParsedFyFiles_UsingFyParser_PropertyMixin,
    MixinImportMap_UsingParsedFyFiles_PropertyMixin,
    # Method Mixins
    GeneratePyFiles_UsingJinja2Templates_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        self._generate_py_files()

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
