"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseAbstractPropertyFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property abstract_property_file_split using abstract_property_regex
"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.fy_py_template_models import AbstractPropertyTemplateModel
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedAbstractPropertyFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.abstract_property_file_split.using_abstract_property_regex_fy import (
    AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin,
)
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


# fy:start <<<===
class ParseAbstractPropertyFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    AbstractPropertyFileSplit_UsingAbstractPropertyRegex_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===

        assert (
            len(self._abstract_property_file_split) == 4
        ), f"Abstract property file split length {len(self._abstract_property_file_split)} is invalid"

        user_imports = self._abstract_property_file_split[0]
        abstract_property_name = PythonEntityName.from_snake_case(
            self._abstract_property_file_split[1]
        )
        property_type = self._abstract_property_file_split[2]

        parsed_fy_py_file = ParsedAbstractPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=user_imports,
            template_model=AbstractPropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"With_{abstract_property_name.pascal_case}_PropertyMixin_ABC"
                ),
                abstract_property_name=abstract_property_name,
                property_type=property_type,
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
