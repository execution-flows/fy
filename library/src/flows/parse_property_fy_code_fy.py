"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParsePropertyFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property property_file_split using property_regex
"""

import re
from pathlib import Path
from typing import Any, List

from base.flow_base import FlowBase
from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import PropertyTemplateModel, AbstractPropertyModel
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedPropertyFyPyFile
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
from mixins.property.property_file_split.usign_property_regex_fy import (
    PropertyFileSplit_UsingPropertyRegex_PropertyMixin,
)


# fy:start <<<===
class ParsePropertyFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    PropertyFileSplit_UsingPropertyRegex_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        assert (
            len(self._property_file_split) == 6
        ), f"Property file split length {len(self._property_file_split)} is invalid"

        user_imports = self._property_file_split[0]
        property_name = PythonEntityName.from_snake_case(self._property_file_split[2])
        property_type = self._property_file_split[3]
        implementation_name = PythonEntityName.from_snake_case(
            self._property_file_split[4]
        )

        abstract_properties: List[AbstractPropertyModel] = []

        abstract_property_mixin_regex = re.compile(
            rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        )

        check_if_cached = self._property_file_split[1]

        mixin_lines = self._property_file_split[5].split("\n")
        for mixin_line in mixin_lines:
            if mixin_line.strip() == "":
                continue

            declared_abstract_property_mixin = abstract_property_mixin_regex.search(
                mixin_line
            )
            if declared_abstract_property_mixin is not None:
                abstract_properties.append(
                    AbstractPropertyModel(
                        property_name=PythonEntityName.from_snake_case(
                            declared_abstract_property_mixin.group(
                                "abstract_property_name"
                            )
                        )
                    )
                )
                continue

        parsed_fy_py_file = ParsedPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=user_imports,
            template_model=PropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
                ),
                property_name=property_name,
                implementation_name=implementation_name,
                abstract_property_mixins=abstract_properties,
                property_type=property_type,
                property_annotation=("@cached_property" if check_if_cached else None),
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
