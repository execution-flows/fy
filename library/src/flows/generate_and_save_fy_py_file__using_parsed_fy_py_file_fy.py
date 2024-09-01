# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingParsedFyPyFile -> None:
    property parsed_fy_py_file using setter
    property mixin_import_map using setter
    property mixin_imports using parsed_fy_py_file
    property jinja2_template_file_name using parsed_fy_py_file
    method generate_fy_py_code using jinja2_templates
"""
from typing import List, Set, Any, Dict

from base.flow_base import FlowBase
from constants import (
    IMPORT_REGEX,
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    NEW_LINE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from mixins.method.generate_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
)
from mixins.property.jinja2_template_file_name.using_parsed_fy_py_file_fy import (
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.mixin_import_map.using_setter import (
    MixinImportMap_UsingSetter_PropertyMixin,
)
from mixins.property.mixin_imports.using_parsed_fy_py_file_fy import (
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
)
from mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class GenerateAndSaveFyPyFile_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    MixinImportMap_UsingSetter_PropertyMixin,
    MixinImports_UsingParsedFyPyFile_PropertyMixin,
    Jinja2TemplateFileName_UsingParsedFyPyFile_PropertyMixin,
    # Method Mixins
    GenerateFyPyCode_UsingJinja2Templates_MethodMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        generated_python_code = self.__match_kind__and__load_fy_py_files()

        filtered_mixin_imports = remove_existing_imports(
            mixin_imports=self._mixin_imports,
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

    def __match_kind__and__load_fy_py_files(self) -> str:
        return self._generate_fy_py_code(
            jinja2_template=self._jinja2_template_file_name,
            template_model=self._parsed_fy_py_file.template_model,
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
