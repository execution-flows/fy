# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile


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

from fy_library.domain.fy_py_template_models import TemporaryBaseTemplateModel
from fy_library.domain.parsed_fy_py_file import ParsedAbstractPropertyFyPyFile
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.abstract_property_file_split.abc_fy import (
    AbstractPropertyFileSplit_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
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

from fy_library.mixins.property.parsed_abstract_property_fy_py_file.abc_fy import (
    ParsedAbstractPropertyFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedAbstractPropertyFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    AbstractPropertyFileSplit_PropertyMixin_ABC,
    FyCode_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    ParsedAbstractPropertyFyPyFile_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    PreFyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
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
            abstract_property_name=abstract_property_name,
            generics_def=self._abstract_property_file_split.generics_def,
            property_type=self._abstract_property_file_split.property_type,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{abstract_property_name.pascal_case}_PropertyMixin_ABC"
            ),
            template_model=TemporaryBaseTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{abstract_property_name.pascal_case}_PropertyMixin_ABC"
                ),
                entity_key_value=abstract_property_name.snake_case,
            ),
        )

        return parsed_fy_py_file
