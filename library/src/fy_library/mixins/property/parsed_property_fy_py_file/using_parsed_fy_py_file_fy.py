# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile


property parsed_property_fy_py_file: ParsedPropertyFyPyFile using parsed_fy_py_file:
    property pre_fy_code
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property property_file_split
    property included_mixins
"""

import abc
from functools import cached_property

from fy_library.domain.fy_py_template_models import (
    TemporaryBaseTemplateModel,
)
from fy_library.domain.parsed_fy_py_file import ParsedPropertyFyPyFile
from fy_library.domain.entity_key import entity_key
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from fy_library.mixins.property.included_mixins.abc_fy import (
    IncludedMixins_PropertyMixin_ABC,
)
from fy_library.mixins.property.post_marker_file_content.abc_fy import (
    PostMarkerFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.pre_fy_code.abc_fy import (
    PreFyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.pre_marker_file_content.abc_fy import (
    PreMarkerFileContent_PropertyMixin_ABC,
)
from fy_library.mixins.property.property_file_split.abc_fy import (
    PropertyFileSplit_PropertyMixin_ABC,
)

from fy_library.mixins.property.parsed_property_fy_py_file.abc_fy import (
    ParsedPropertyFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    IncludedMixins_PropertyMixin_ABC,
    ParsedPropertyFyPyFile_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    PreFyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
    PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_property_fy_py_file(self) -> ParsedPropertyFyPyFile:
        # fy:end <<<===
        property_name = PythonEntityName.from_snake_case(
            self._property_file_split.property_name
        )
        implementation_name = PythonEntityName.from_snake_case(
            self._property_file_split.implementation_name
        )

        parsed_fy_py_file = ParsedPropertyFyPyFile(
            pre_fy_code=self._pre_fy_code,
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._property_file_split.user_imports,
            property_name=property_name,
            implementation_name=implementation_name,
            abstract_property_mixins=self._included_mixins.abstract_property_mixins,
            generics_def=self._property_file_split.generics_def,
            property_type=self._property_file_split.property_type,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
            ),
            template_model=TemporaryBaseTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
                ),
                entity_key_value=entity_key(
                    mixin_name__snake_case=property_name.snake_case,
                    mixin_implementation_name__snake_case=implementation_name.snake_case,
                ),
            ),
        )

        return parsed_fy_py_file
