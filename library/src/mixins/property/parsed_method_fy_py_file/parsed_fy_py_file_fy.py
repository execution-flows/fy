"""fy
from domain.parsed_fy_py_file import ParsedMethodFyPyFile


property parsed_method_fy_py_file: ParsedMethodFyPyFile using parsed_fy_py_file:
    property pre_fy_code
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property method_file_split
    property included_mixins
"""

import abc
from functools import cached_property

from domain.fy_py_template_models import MethodTemplateModel
from domain.parsed_fy_py_file import ParsedMethodFyPyFile
from domain.python_entity_name import PythonEntityName


from mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.included_mixins.abc_fy import (
    IncludedMixins_PropertyMixin_ABC,
)
from mixins.property.method_file_split.abc_fy import (
    MethodFileSplit_PropertyMixin_ABC,
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
class ParsedMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    PreFyCode_PropertyMixin_ABC,
    FyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    MethodFileSplit_PropertyMixin_ABC,
    IncludedMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_method_fy_py_file(self) -> ParsedMethodFyPyFile:
        # fy:end <<<===

        method_name = PythonEntityName.from_snake_case(
            self._method_file_split.method_name
        )
        implementation_name = PythonEntityName.from_snake_case(
            self._method_file_split.implementation_name
        )

        parsed_fy_py_file = ParsedMethodFyPyFile(
            pre_fy_code=self._pre_fy_code,
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._method_file_split.user_imports,
            template_model=MethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
                ),
                method_name=method_name,
                implementation_name=implementation_name,
                abstract_property_mixins=self._included_mixins.abstract_property_mixins,
                abstract_method_mixins=self._included_mixins.abstract_method_mixins,
                arguments=self._method_file_split.arguments,
                return_type=self._method_file_split.return_type,
            ),
        )

        return parsed_fy_py_file
