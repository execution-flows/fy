from typing import List, Tuple, Set
import re
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
            generated_python_code, mixin_imports = (
                self.__match_kind__and__load_fy_py_files(parsed_fy_py_file)
            )
            filtered_mixin_imports = remove_existing_imports(
                mixin_imports=mixin_imports,
                pre_marker_file_content=parsed_fy_py_file.pre_marker_file_content,
            )
            mixin_imports_code = "\n".join(
                filtered_mixin_imports
                + (["", "", ""] if filtered_mixin_imports else [])
            )
            fy_py_file_content = (
                f"{FY_PY_FILE_SIGNATURE}"
                f"{parsed_fy_py_file.fy_code}"
                f"{FY_CODE_FILE_END_SIGNATURE}\n"
                f"{parsed_fy_py_file.pre_marker_file_content}"
                f"{mixin_imports_code}"
                f"{FY_START_MARKER}\n"
                f"{generated_python_code}"
                f"{FY_END_MARKER}\n"
                f"{parsed_fy_py_file.post_marker_file_content}"
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
            case ParsedFyPyFileKind.METHOD:
                mixin_imports = []
                return (
                    generated_fy_py_code(
                        jinja2_template="method.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports
                )
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                mixin_imports = ["import abc"]
                return (
                    generated_fy_py_code(
                        jinja2_template="abstract_method.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
        raise ValueError(f"No Execution Flow kind for {parsed_fy_py_file.file_type}")


IMPORT_REGEX = re.compile(
    r"^(?P<from>from [\w.]+) import .*$|^(?P<import>import [\w.]+)$"
)


def remove_existing_imports(
    mixin_imports: List[str], pre_marker_file_content: str
) -> List[str]:
    pre_marker_imports: Set[str] = set()
    for pre_marker_line in pre_marker_file_content.split("\n"):
        import_regex_result = IMPORT_REGEX.search(pre_marker_line)
        if import_regex_result is not None:
            pre_marker_imports.add(
                import_regex_result.group("from") or import_regex_result.group("import")
            )

    mixin_imports_result = []
    for mixin_import in mixin_imports:
        import_regex_result = IMPORT_REGEX.search(mixin_import)
        import_part = import_regex_result.group("from") or import_regex_result.group(
            "import"
        )
        if import_part not in pre_marker_imports:
            mixin_imports_result.append(mixin_import)

    return mixin_imports_result


def generated_fy_py_code(
    jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
) -> str:
    templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template)
    template_model = parsed_fy_py_file.template_model.model_dump()
    content = template.render(template_model)
    return content
