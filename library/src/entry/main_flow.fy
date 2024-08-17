from pathlib import Path
from typing import Any

flow Main:
    property folder_to_parse using setter
    property project_root_folder using setter
    property fy_files_to_parse using files_discovery
    property parsed_fy_files using fy_parser
    property mixin_import_map using parsed_fy_files

    method generate_py_files using jinja2_templates

    def -> None:
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
