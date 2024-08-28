"""fy
from domain.parsed_fy_py_file import ParsedPropertyFyPyFile


property parsed_property_fy_py_file: ParsedPropertyFyPyFile using parsed_fy_py_file:
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property property_file_split
    property property_mixins
"""

import abc

from domain.fy_py_template_models import PropertyTemplateModel
from domain.parsed_fy_py_file import ParsedPropertyFyPyFile
from domain.python_entity_name import PythonEntityName

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
from mixins.property.property_file_split.abc_fy import (
    With_PropertyFileSplit_PropertyMixin_ABC,
)


from mixins.property.property_mixins.abc_fy import (
    With_PropertyMixins_PropertyMixin_ABC,
)


# fy:start <<<===
class ParsedPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_PropertyFileSplit_PropertyMixin_ABC,
    With_PropertyMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        # fy:end <<<===
        property_name = PythonEntityName.from_snake_case(self._property_file_split[2])
        implementation_name = PythonEntityName.from_snake_case(
            self._property_file_split[4]
        )

        parsed_fy_py_file = ParsedPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._property_file_split[0],
            template_model=PropertyTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
                ),
                property_name=property_name,
                implementation_name=implementation_name,
                abstract_property_mixins=self._property_mixins,
                property_type=self._property_file_split[3],
                property_annotation=(
                    "@cached_property" if self._property_file_split[1] else None
                ),
            ),
        )

        return parsed_fy_py_file
