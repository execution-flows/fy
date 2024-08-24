from typing import Dict
from domain.parsed_fy_py_file import ParsedFyPyFile


property mixin_import_map using parsed_fy_py_files:
    with property parsed_fy_py_files
    with property required_property_setters_fy_py
    with property project_root_folder

    @cached
    def -> Dict[str, str]:
        mixin_import_map = {
            parsed_fy_py_file.template_model.entity_key: self.__parsed_file_python_import(
                parsed_fy_py_file
            )
            for parsed_fy_py_file in self._parsed_fy_py_files
        }
        return mixin_import_map

    def __parsed_file_python_import(self, parsed_fy_py_file: ParsedFyPyFile) -> str:
        relative_file_folder_path = parsed_fy_py_file.file_path.parent.relative_to(
            self._project_root_folder
        )
        file_name = parsed_fy_py_file.file_path.stem
        python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
        return f"from {python_file_path} import (\n{' ' * 4}{parsed_fy_py_file.template_model.python_class_name.pascal_case},\n)"
