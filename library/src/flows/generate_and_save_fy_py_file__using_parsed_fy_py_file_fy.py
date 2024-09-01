# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow GenerateAndSaveFyPyFile_UsingParsedFyPyFile -> None:
    property parsed_fy_py_file using setter
    property mixin_import_map using setter
    property mixin_imports using parsed_fy_py_file
    property jinja2_template_file_name using parsed_fy_py_file
    property generate_fy_py_code using jinja2_templates
    property filtered_mixin_imports using remove_existing_imports
"""
from typing import Any, Dict

from base.flow_base import FlowBase
from constants import (
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
    NEW_LINE,
    FY_START_MARKER,
    FY_END_MARKER,
)
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
)
from mixins.property.filtered_mixin_imports.remove_existing_imports_fy import (
    FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin,
)
from mixins.property.generated_fy_py_code.using_jinja2_templates_fy import (
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
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
    GenerateFyPyCode_UsingJinja2Templates_PropertyMixin,
    FilteredMixinImports_UsingRemoveExistingImports_PropertyMixin,
    # Base
    FlowBase[None],
):
    def __call__(self) -> None:
        # fy:end <<<===
        mixin_imports_code = "\n".join(
            sorted(self._filtered_mixin_imports)
            + ([""] if self._filtered_mixin_imports else [])
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
            f"{self._generate_fy_py_code}"
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
