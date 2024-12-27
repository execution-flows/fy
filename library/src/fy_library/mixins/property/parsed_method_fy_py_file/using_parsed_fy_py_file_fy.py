# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedMethodFyPyFile


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

from fy_library.domain.fy_py_template_models import (
    TemporaryBaseTemplateModel,
)
from fy_library.domain.parsed_fy_py_file import ParsedMethodFyPyFile
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
from fy_library.mixins.property.method_file_split.abc_fy import (
    MethodFileSplit_PropertyMixin_ABC,
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

from fy_library.mixins.property.parsed_method_fy_py_file.abc_fy import (
    ParsedMethodFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedMethodFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    IncludedMixins_PropertyMixin_ABC,
    MethodFileSplit_PropertyMixin_ABC,
    ParsedMethodFyPyFile_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    PreFyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
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
            method_name=method_name,
            abstract_property_mixins=self._included_mixins.abstract_property_mixins,
            abstract_method_mixins=self._included_mixins.abstract_method_mixins,
            generics_def=self._method_file_split.generics_def,
            arguments=self._method_file_split.arguments,
            return_type=self._method_file_split.return_type,
            implementation_name=implementation_name,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
            ),
            template_model=TemporaryBaseTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
                ),
                entity_key_value=entity_key(
                    mixin_name__snake_case=method_name.snake_case,
                    mixin_implementation_name__snake_case=implementation_name.snake_case,
                ),
            ),
        )

        return parsed_fy_py_file
