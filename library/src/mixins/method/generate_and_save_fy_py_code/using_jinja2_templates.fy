from typing import List
from jinja2 import Environment, FileSystemLoader
import pathlib
from domain.parsed_fy_py_file import ParsedFyPyFileKind, ParsedFyPyFile
from constants import FY_PY_FILE_SIGNATURE, FY_CODE_FILE_END_SIGNATURE, FY_END_MARKER, FY_START_MARKER


method generate_and_save_fy_py_files using jinja2_templates:
    with property parsed_fy_py_files
    with property required_property_setters_fy_py
    with property mixin_import_map

    def -> None:
                for parsed_fy_py_file in self._parsed_fy_py_files:
            generated_python_code = self.__match_kind__and__load_fy_py_files(
                parsed_fy_py_file
            )
            mixin_imports = "\n".join(generated_python_code[1]) + "\n"
            fy_py_file_content = (
                f"{FY_PY_FILE_SIGNATURE}"
                f"{parsed_fy_py_file.fy_code}"
                f"{FY_CODE_FILE_END_SIGNATURE}\n"
                f"{mixin_imports}"
                f"{FY_START_MARKER}\n"
                f"{generated_python_code[0]}\n"
                f"{FY_END_MARKER}\n"
                f"{parsed_fy_py_file.post_marker_file_content}\n"
            )
            with open(
                file=parsed_fy_py_file.file_path, mode="w", encoding="UTF-8"
            ) as output_py_file:
                output_py_file.write(fy_py_file_content)

    def __match_kind__and__load_fy_py_files(
        self, parsed_fy_py_file: ParsedFyPyFile
    ) -> Tuple[str, List[str]]:
        match parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                mixin_imports = [
                    "from base.execution_flow_base import ExecutionFlowBase",
                ]
                return (
                    generated_fy_py_code(
                        jinja2_template="flow.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
                )

        raise ValueError(f"No Execution Flow kind for {parsed_fy_py_file.file_type}")


def generated_fy_py_code(
    jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
) -> str:
    templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template)
    template_model = parsed_fy_py_file.template_model.model_dump()
    content = template.render(template_model)
    return content
