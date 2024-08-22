from typing import Dict


property mixin_import_map using parsed_fy_py_files:
    with property parsed_fy_py_files
    with property required_property_setters_fy_py
    with property project_root_folder

    @cached
    def -> Dict[str, str]:
        return {}