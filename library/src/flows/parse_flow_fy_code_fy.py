"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseFlowFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property flow_file_split using flow_regex
    property mixin_lines using flow_file_split
    property property_mixins using flow_mixin_lines
    property method_mixins using flow_mixin_lines
"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.fy_py_template_models import (
    FlowTemplateModel,
)
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFlowFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.flow_file_split.using_flow_regex_fy import (
    FlowFileSplit_UsingFlowRegex_PropertyMixin,
)
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.mixin_lines.using_flow_file_split_fy import (
    MixinLines_UsingFlowFileSplit_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.property_mixins.using_flow_mixin_lines_fy import (
    PropertyMixins_UsingFlowMixinLines_PropertyMixin,
)
from mixins.property.method_mixins.using_flow_mixin_lines_fy import (
    MethodMixins_UsingFlowMixinLines_PropertyMixin,
)


# fy:start ===>>>
class ParseFlowFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    FlowFileSplit_UsingFlowRegex_PropertyMixin,
    MixinLines_UsingFlowFileSplit_PropertyMixin,
    PropertyMixins_UsingFlowMixinLines_PropertyMixin,
    MethodMixins_UsingFlowMixinLines_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===

        flow_name = PythonEntityName.from_pascal_case(self._flow_file_split.flow_name)

        parsed_fy_py_file = ParsedFlowFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._flow_file_split.user_imports,
            template_model=FlowTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{flow_name.pascal_case}_Flow"
                ),
                flow_name=flow_name,
                return_type=self._flow_file_split.return_type,
                properties=self._property_mixins,
                methods=self._method_mixins,
            ),
        )

        return parsed_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        pre_marker_file_content: str,
        post_marker_file_content: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        self._fy_py_file_to_parse = fy_py_file_to_parse
        self._pre_marker_file_content = pre_marker_file_content
        self._post_marker_file_content = post_marker_file_content
        super().__init__(*args, **kwargs)
