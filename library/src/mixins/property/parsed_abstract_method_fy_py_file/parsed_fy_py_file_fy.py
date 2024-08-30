"""fy
from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile


property parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile using  parsed_fy_py_file:
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property abstract_method_file_split
"""

import abc
from functools import cached_property

from domain.fy_py_template_models import AbstractMethodTemplateModel
from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile
from domain.python_entity_name import PythonEntityName


from mixins.property.abstract_method_file_split.abc_fy import (
    AbstractMethodFileSplit_PropertyMixin_ABC,
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


# fy:start ===>>>
class ParsedAbstractMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    AbstractMethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_abstract_method_fy_py_file(self) -> ParsedAbstractMethodFyPyFile:
        # fy:end <<<===
        abstract_method_name = PythonEntityName.from_snake_case(
            self._abstract_method_file_split.abstract_method_name
        )

        parsed_fy_py_file = ParsedAbstractMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._abstract_method_file_split.user_imports,
            template_model=AbstractMethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{abstract_method_name.pascal_case}_MethodMixin_ABC"
                ),
                abstract_method_name=abstract_method_name,
                arguments=self._abstract_method_file_split.arguments,
                return_type=self._abstract_method_file_split.return_type,
            ),
        )

        return parsed_fy_py_file
