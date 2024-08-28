"""fy
from domain.parsed_fy_py_file import ParsedMethodFyPyFile


property parsed_method_fy_py_file: ParsedMethodFyPyFile using parsed_fy_py_file:
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property method_file_split
    property declared_abstract_property_mixins
    property declared_abstract_method_mixins
"""

import abc

from domain.fy_py_template_models import MethodTemplateModel
from domain.parsed_fy_py_file import ParsedMethodFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.declared_abstract_method_mixins.abc_fy import (
    With_DeclaredAbstractMethodMixins_PropertyMixin_ABC,
)
from mixins.property.declared_abstract_property_mixins.abc_fy import (
    With_DeclaredAbstractPropertyMixins_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.method_file_split.abc_fy import (
    With_MethodFileSplit_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc_fy import (
    With_PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.pre_marker_file_content.abc_fy import (
    With_PreMarkerFileContent_PropertyMixin_ABC,
)


# fy:start <<<===
class ParsedMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_MethodFileSplit_PropertyMixin_ABC,
    With_DeclaredAbstractPropertyMixins_PropertyMixin_ABC,
    With_DeclaredAbstractMethodMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _parsed_method_fy_py_file(self) -> ParsedMethodFyPyFile:
        # fy:end <<<===

        method_name = PythonEntityName.from_snake_case(self._method_file_split[1])
        implementation_name = PythonEntityName.from_snake_case(
            self._method_file_split[5]
        )

        parsed_fy_py_file = ParsedMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._method_file_split[0],
            template_model=MethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
                ),
                method_name=method_name,
                implementation_name=implementation_name,
                abstract_property_mixins=self._declared_abstract_property_mixins,
                abstract_method_mixins=self._declared_abstract_method_mixins,
                arguments=self._method_file_split[3],
                return_type=self._method_file_split[4],
            ),
        )

        return parsed_fy_py_file
