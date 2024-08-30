"""fy
from domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile


property parsed_abstract_property_fy_py_file: ParsedAbstractPropertyFyPyFile using parsed_fy_py_file:
    property pre_fy_code
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
    AbstractPropertyFileSplit_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc_fy import (
    PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.pre_marker_file_content.abc_fy import (
    PreMarkerFileContent_PropertyMixin_ABC,
)


from mixins.property.pre_fy_code.abc_fy import (
    PreFyCode_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedAbstractPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    PreFyCode_PropertyMixin_ABC,
    FyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    AbstractPropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_abstract_property_fy_py_file(self) -> ParsedAbstractPropertyFyPyFile:
        # fy:end <<<===
        abstract_property_name = PythonEntityName.from_snake_case(
            self._abstract_property_file_split.abstract_property_name
        )

        parsed_fy_py_file = ParsedAbstractPropertyFyPyFile(
            pre_fy_code=self._pre_fy_code,
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._abstract_property_file_split.user_imports,
            template_model=AbstractPropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{abstract_property_name.pascal_case}_PropertyMixin_ABC"
                ),
                abstract_property_name=abstract_property_name,
                property_type=self._abstract_property_file_split.property_type,
            ),
        )

        return parsed_fy_py_file
