"""fy
from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile


property parsed_abstract_method_fy_py_file: ParsedAbstractMethodFyPyFile using  parsed_fy_py_file:
    with property fy_code
    with property pre_marker_file_content
    with property post_marker_file_content
    with property fy_py_file_to_parse
    with property abstract_method_file_split
"""

from domain.fy_py_template_models import AbstractMethodTemplateModel
from domain.parsed_fy_py_file import ParsedAbstractMethodFyPyFile
from domain.python_entity_name import PythonEntityName

from mixins.property.abstract_method_file_split.abc_fy import (
    With_AbstractMethodFileSplit_PropertyMixin_ABC,
)
import abc


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
class ParsedAbstractMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_AbstractMethodFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _parsed_abstract_method_fy_py_file(self) -> ParsedAbstractMethodFyPyFile:
        # fy:end <<<===
        abstract_method_file_split = self._abstract_method_file_split

        abstract_method_name = PythonEntityName.from_snake_case(
            abstract_method_file_split[1]
        )

        parsed_fy_py_file = ParsedAbstractMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=abstract_method_file_split[0],
            template_model=AbstractMethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"With_{abstract_method_name.pascal_case}_MethodMixin_ABC"
                ),
                abstract_method_name=abstract_method_name,
                arguments=abstract_method_file_split[3],
                return_type=abstract_method_file_split[4],
            ),
        )

        return parsed_fy_py_file
