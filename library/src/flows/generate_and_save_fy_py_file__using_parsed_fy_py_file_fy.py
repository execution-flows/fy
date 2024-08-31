# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingParsedFyPyFile -> None:
    property parsed_fy_py_file using setter
    property mixin_import_map using setter

    method generate_fy_py_code using jinja2_templates
"""
from typing import List, Set, Tuple, cast, Any, Dict

from base.flow_base import FlowBase
from constants import (
    IMPORT_REGEX,
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    NEW_LINE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from domain.fy_py_template_models import entity_key
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedFyPyFileKind,
    ParsedFlowFyPyFile,
    ParsedMethodFyPyFile,
    ParsedPropertyFyPyFile,
)
from mixins.method.generate_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
)
from mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    # Method Mixins
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        generated_python_code, mixin_imports = (
            self.__match_kind__and__load_fy_py_files()
        )

        filtered_mixin_imports = remove_existing_imports(
            mixin_imports=mixin_imports,
            pre_marker_file_content=self._parsed_fy_py_file.pre_marker_file_content,
            user_imports=self._parsed_fy_py_file.user_imports,
        )
        mixin_imports_code = "\n".join(
            sorted(filtered_mixin_imports) + ([""] if filtered_mixin_imports else [])
        )

        fy_py_file_content = (
            f"{self._parsed_fy_py_file.pre_fy_code}"
            f"{FY_PY_FILE_SIGNATURE}"
            f"{self._parsed_fy_py_file.fy_code}"
            f"{FY_CODE_FILE_END_SIGNATURE}\n"
            f"{self._parsed_fy_py_file.pre_marker_file_content}"
            f"{NEW_LINE if not self._parsed_fy_py_file.pre_marker_file_content or mixin_imports_code else ''}"
            f"{mixin_imports_code}"
            f"{NEW_LINE * 2 if not self._parsed_fy_py_file.pre_marker_file_content or mixin_imports_code else ''}"
            f"{FY_START_MARKER}\n"
            f"{generated_python_code}"
            f"{FY_END_MARKER}\n"
            f"{self._parsed_fy_py_file.post_marker_file_content}"
        )
        with open(
            file=self._parsed_fy_py_file.file_path, mode="w", encoding="UTF-8"
        ) as output_py_file:
            output_py_file.write(fy_py_file_content)

    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        mixin_import_map: Dict[str, str],
        **kwargs: Any,
    ):
        self._mixin_import_map = mixin_import_map
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)

    def __match_kind__and__load_fy_py_files(self) -> Tuple[str, List[str]]:
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                mixin_imports = (
                    [
                        # static imports
                        "from base.flow_base import FlowBase",
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
                            ParsedFlowFyPyFile, self._parsed_fy_py_file
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
                            ParsedFlowFyPyFile, self._parsed_fy_py_file
                        ).template_model.methods
                    ]
                )

                return (
                    self._generate_fy_py_code(
                        jinja2_template="flow.jinja2",
                        parsed_fy_py_file=self._parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.METHOD:
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                        or cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
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
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                    + [
                        # method mixins
                        self._mixin_import_map[
                            abstract_method_mixin.method_name.snake_case
                        ]
                        for abstract_method_mixin in cast(
                            ParsedMethodFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_method_mixins
                    ]
                )
                return (
                    self._generate_fy_py_code(
                        jinja2_template="method.jinja2",
                        parsed_fy_py_file=self._parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.ABSTRACT_METHOD:
                mixin_imports = ["import abc"]
                return (
                    self._generate_fy_py_code(
                        jinja2_template="abstract_method.jinja2",
                        parsed_fy_py_file=self._parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.ABSTRACT_PROPERTY:
                mixin_imports = ["import abc"]
                return (
                    self._generate_fy_py_code(
                        jinja2_template="abstract_property.jinja2",
                        parsed_fy_py_file=self._parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
            case ParsedFyPyFileKind.PROPERTY:
                static_imports = (
                    ["import abc"]
                    if (
                        cast(
                            ParsedPropertyFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    )
                    else []
                )
                cached_import = ["from functools import cached_property"]
                mixin_imports = (
                    cached_import
                    + static_imports
                    + [
                        # property mixins
                        self._mixin_import_map[
                            abstract_property_mixin.property_name.snake_case
                        ]
                        for abstract_property_mixin in cast(
                            ParsedPropertyFyPyFile, self._parsed_fy_py_file
                        ).template_model.abstract_property_mixins
                    ]
                )
                return (
                    self._generate_fy_py_code(
                        jinja2_template="property.jinja2",
                        parsed_fy_py_file=self._parsed_fy_py_file,
                    ),
                    mixin_imports,
                )
        raise ValueError(
            f"No Execution Flow kind for {self._parsed_fy_py_file.file_type}"
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
