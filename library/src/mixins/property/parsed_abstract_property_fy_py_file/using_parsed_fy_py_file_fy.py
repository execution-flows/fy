"""fy
from domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile


property parsed_abstract_property_fy_py_file: ParsedAbstractPropertyFyPyFile using parsed_fy_py_file:
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property abstract_property_file_split
"""

import abc
from functools import cached_property

from domain.fy_py_template_models import AbstractPropertyTemplateModel
from domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.abstract_property_file_split.abc_fy import (
    With_AbstractPropertyFileSplit_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc_fy import (
    With_PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.pre_marker_file_content.abc_fy import (
    With_PreMarkerFileContent_PropertyMixin_ABC,
)


# fy:start <<<===
class ParsedAbstractPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_AbstractPropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_abstract_property_fy_py_file(self) -> ParsedAbstractPropertyFyPyFile:
        # fy:end <<<===
        abstract_property_name = PythonEntityName.from_snake_case(
            self._abstract_property_file_split[1]
        )

        parsed_fy_py_file = ParsedAbstractPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._abstract_property_file_split[0],
            template_model=AbstractPropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"With_{abstract_property_name.pascal_case}_PropertyMixin_ABC"
                ),
                abstract_property_name=abstract_property_name,
                property_type=self._abstract_property_file_split[2],
            ),
        )

        return parsed_fy_py_file
