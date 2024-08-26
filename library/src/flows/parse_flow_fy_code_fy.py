"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseFlowFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
"""

from base.flow_base import FlowBase
from constants import FY_ENTITY_REGEX_STRING, PYTHON_MULTI_ENTITY_REGEX_STRING
from domain.fy_py_template_models import (
    FlowTemplateModel,
    PropertyMixinModel,
    MethodMixinModel,
)
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedFlowFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)
from pathlib import Path
from typing import Any, List
import re


# fy:start <<<===
class ParseFlowFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        flow_string_split_regex = re.compile(
            rf"flow\s+(?P<flow_name>{FY_ENTITY_REGEX_STRING})\s+->"
            rf"\s+(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING}):\s*\n"
        )

        flow_file_split = flow_string_split_regex.split(self._fy_code)

        assert (
            len(flow_file_split)
        ) == 4, f"Flow file split length {len(flow_file_split)} is invalid."

        user_imports = flow_file_split[0]
        flow_name = PythonEntityName.from_pascal_case(flow_file_split[1])
        return_type = flow_file_split[2]

        properties: List[PropertyMixinModel] = []
        methods: List[MethodMixinModel] = []
        mixin_lines = flow_file_split[3].split("\n")
        for mixin_line in mixin_lines:
            if mixin_line.strip() == "":
                continue

            flow_property_regex = re.compile(
                pattern=rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
                rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
            )
            flow_property_fy_search = flow_property_regex.search(mixin_line)
            if flow_property_fy_search:
                properties.append(
                    PropertyMixinModel(
                        property_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("property_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("implementation_name")
                        ),
                    )
                )
            flow_method_regex = re.compile(
                pattern=rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
                rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
            )
            flow_method_fy_search = flow_method_regex.search(mixin_line)

            if flow_method_fy_search:
                methods.append(
                    MethodMixinModel(
                        method_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("method_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("implementation_name")
                        ),
                    )
                )

        parsed_fy_py_file = ParsedFlowFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=user_imports,
            template_model=FlowTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{flow_name.pascal_case}_Flow"
                ),
                flow_name=flow_name,
                return_type=return_type,
                properties=properties,
                methods=methods,
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
