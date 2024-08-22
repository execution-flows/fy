from base.execution_flow_base import ExecutionFlowBase

from mixins.property.folder_to_parse.using_setter import (
    FolderToParse_UsingSetter_PropertyMixin,
)
from mixins.property.project_root_folder.using_setter import (
    ProjectRootFolder_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_files_to_parse.using_files_discovery import (
    FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin,
)
from mixins.property.parsed_fy_py_files.using_fy_py_parser import (
    ParsedFyPyFiles_UsingFyPyParser_PropertyMixin,
)
from mixins.property.parsed_fy_py_files_map_by_key.using_parsed_fy_py_files import (
    ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin,
)
from mixins.property.required_property_setters_fy_py.using_parsed_fy_py_files import (
    RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin,
)
from mixins.property.mixin_import_map.using_parsed_fy_py_files import (
    MixinImportMap_UsingParsedFyPyFiles_PropertyMixin,
)
from mixins.method.generate_and_save_fy_py_code.using_jinja2_templates import (
    GenerateAndSaveFyPyFiles_UsingJinja2Templates_MethodMixin,
)

from pathlib import Path
from typing import Any


class FyPy_Main_Flow(
    # Property Mixins
    FolderToParse_UsingSetter_PropertyMixin,
    ProjectRootFolder_UsingSetter_PropertyMixin,
    FyPyFilesToParse_UsingFilesDiscovery_PropertyMixin,
    ParsedFyPyFiles_UsingFyPyParser_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingParsedFyPyFiles_PropertyMixin,
    RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin,
    MixinImportMap_UsingParsedFyPyFiles_PropertyMixin,
    # Method Mixins
    GenerateAndSaveFyPyFiles_UsingJinja2Templates_MethodMixin,
    # Base
    ExecutionFlowBase[None],
):
    def __call__(self) -> None:
        self._generate_and_save_fy_py_files()

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
