import abc

from mixins.property.parsed_fy_py_files.abc import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.required_property_setters_fy_py.abc import (
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
)
from mixins.property.mixin_import_map.abc import With_MixinImportMap_PropertyMixin_ABC

from typing import List, Tuple, Set, cast
import re
from jinja2 import Environment, FileSystemLoader
import pathlib
from domain.fy_py_template_models import entity_key
from domain.parsed_fy_py_file import (
    ParsedFyPyFileKind,
    ParsedFyPyFile,
    ParsedFlowFyPyFile,
    ParsedMethodFyPyFile,
    ParsedPropertyFyPyFile,
)
from constants import (
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    FY_END_MARKER,
    FY_START_MARKER,
    NEW_LINE,
)


class GenerateAndSaveFyPyFiles_UsingJinja2Templates_MethodMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
    With_MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_fy_py_files(self) -> None:
        for parsed_fy_py_file in self._parsed_fy_py_files:
            generated_python_code, mixin_imports = (
                self.__match_kind__and__load_fy_py_files(parsed_fy_py_file)
            )
            filtered_mixin_imports = remove_existing_imports(
                mixin_imports=mixin_imports,
                pre_marker_file_content=parsed_fy_py_file.pre_marker_file_content,
                user_imports=parsed_fy_py_file.user_imports,
            )
            mixin_imports_code = "\n".join(
                sorted(filtered_mixin_imports)
                + ([""] if filtered_mixin_imports else [])
            )

            fy_py_file_content = (
                f"{FY_PY_FILE_SIGNATURE}"
                f"{parsed_fy_py_file.fy_code}"
                f"{FY_CODE_FILE_END_SIGNATURE}\n"
                f"{parsed_fy_py_file.pre_marker_file_content}"
                f"{mixin_imports_code}"
                f"{NEW_LINE * 2 if not parsed_fy_py_file.pre_marker_file_content or mixin_imports_code else ''}"
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
                mixin_imports = (
                    [
                        # static imports
                        "from base.execution_flow_base import ExecutionFlowBase",
                    ]
                    + [
                        # property mixins
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=property_mixin.property_name.snake_case,
                                mixin_implementation_name__snake_case=property_mixin.implementation_name.snake_case,
                            )
                        ]
                        for property_mixin in cast(
                            ParsedFlowFyPyFile, parsed_fy_py_file
                        ).template_model.properties
                    ]
                    + [
                        # method mixins
                        self._mixin_import_map[
                            entity_key(
                                mixin_name__snake_case=method_mixin.method_name.snake_case,
                                mixin_implementation_name__snake_case=method_mixin.implementation_name.snake_case,
                            )
                        ]
                        for method_mixin in cast(
                            ParsedFlowFyPyFile, parsed_fy_py_file
                        ).template_model.methods
                    ]
                )

                return (
                    generated_fy_py_code(
                        jinja2_template="flow.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.METHOD:
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedMethodFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                        or cast(
                            ParsedMethodFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_method_mixins
                    )
                    else []
                )
                mixin_imports = (
                    static_imports
                    + [
                        # property mixins
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedMethodFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                    + [
                        # method mixins
                        self._mixin_import_map[
                            abstract_method_mixin.method_name.snake_case
                        ]
                        for abstract_method_mixin in cast(
                            ParsedMethodFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_method_mixins
                    ]
                )
                return (
                    generated_fy_py_code(
                        jinja2_template="method.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
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
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                mixin_imports = ["import abc"]
                return (
                    generated_fy_py_code(
                        jinja2_template="abstract_property.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.PROPERTY:
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedPropertyFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    )
                    else []
                )
                cached_import = (
                    ["from functools import cached_property"]
                    if (
                        cast(
                            ParsedPropertyFyPyFile, parsed_fy_py_file
                        ).template_model.property_annotation
                    )
                    else []
                )
                mixin_imports = (
                    cached_import
                    + static_imports
                    + [
                        # property mixins
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedPropertyFyPyFile, parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                )
                return (
                    generated_fy_py_code(
                        jinja2_template="property.jinja2",
                        parsed_fy_py_file=parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
        raise ValueError(f"No Execution Flow kind for {parsed_fy_py_file.file_type}")


IMPORT_REGEX = re.compile(
    r"^(?P<from>from [\w.]+) import .*$|^(?P<import>import [\w.]+)$", flags=re.DOTALL
)


def remove_existing_imports(
    mixin_imports: List[str], pre_marker_file_content: str, user_imports: str
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

    user_imports_results = []
    for user_import in user_imports.split("\n"):
        if user_import == "":
            continue
        import_regex_result = IMPORT_REGEX.search(user_import)
        import_part = import_regex_result.group("from") or import_regex_result.group(
            "import"
        )
        if import_part not in pre_marker_imports:
            user_imports_results.append(user_import)

    return mixin_imports_result + user_imports_results


def generated_fy_py_code(
    jinja2_template: str, parsed_fy_py_file: ParsedFyPyFile
) -> str:
    templates_path = str(pathlib.Path(__file__).parent / "jinja2_templates")
    env = Environment(loader=FileSystemLoader(templates_path))
    template = env.get_template(jinja2_template)
    template_model = parsed_fy_py_file.template_model.model_dump()
    content = template.render(template_model)
    return content
