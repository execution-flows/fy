from typing import Dict

from domain.parsed_fy_file import ParsedFyFile


property mixin_import_map using parsed_fy_files:
    with property parsed_fy_files
    with property required_property_setters
    with property project_root_folder

    @cached
    def -> Dict[str, str]:
        mixin_import_map = {
            parsed_fy_file.template_model.mixin_key: self.__parsed_file_python_import(
                parsed_fy_file
            )
            for parsed_fy_file in self._parsed_fy_files + self._required_property_setters
        }
        return mixin_import_map

    def __parsed_file_python_import(self, parsed_fy_file: ParsedFyFile) -> str:
        relative_file_folder_path = (
            parsed_fy_file.input_fy_file_path.parent.relative_to(
                self._project_root_folder
            )
        )
        file_name = parsed_fy_file.input_fy_file_path.stem
        python_file_path = ".".join(relative_file_folder_path.parts + (file_name,))
        return f"from {python_file_path} import {parsed_fy_file.template_model.python_class_name.pascal_case}"


def mixin_key(
    mixin_name__snake_case: str, mixin_implementation_name__snake_case: str
) -> str:
    return f"{mixin_name__snake_case}.{mixin_implementation_name__snake_case}"
