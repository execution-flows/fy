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
from functools import cached_property

from domain.fy_py_template_models import PropertyTemplateModel
from domain.parsed_fy_py_file import ParsedPropertyFyPyFile
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


# fy:start ===>>>
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
    @cached_property
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        # fy:end <<<===
        parsed_fy_py_file = ParsedPropertyFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._property_file_split.user_imports,
            template_model=PropertyTemplateModel(
                python_class_name=self._property_file_split.python_class_name,
                property_name=self._property_file_split.property_name,
                implementation_name=self._property_file_split.implementation_name,
                abstract_property_mixins=self._property_mixins,
                property_type=self._property_file_split.property_type,
            ),
        )

        return parsed_fy_py_file
