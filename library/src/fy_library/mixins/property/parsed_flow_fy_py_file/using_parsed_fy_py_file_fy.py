# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile


property parsed_flow_fy_py_file: ParsedFlowFyPyFile using parsed_fy_py_file:
    property pre_fy_code
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property flow_file_split
    property included_mixins
"""

import abc
from functools import cached_property

from fy_library.domain.fy_py_template_models import TemporaryBaseTemplateModel
from fy_library.domain.parsed_fy_py_file import ParsedFlowFyPyFile
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.flow_file_split.abc_fy import (
    FlowFileSplit_PropertyMixin_ABC,
)
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

from fy_library.mixins.property.parsed_flow_fy_py_file.abc_fy import (
    ParsedFlowFyPyFile_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFlowFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    FlowFileSplit_PropertyMixin_ABC,
    FyCode_PropertyMixin_ABC,
    FyPyFileToParse_PropertyMixin_ABC,
    IncludedMixins_PropertyMixin_ABC,
    ParsedFlowFyPyFile_PropertyMixin_ABC,
    PostMarkerFileContent_PropertyMixin_ABC,
    PreFyCode_PropertyMixin_ABC,
    PreMarkerFileContent_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_flow_fy_py_file(self) -> ParsedFlowFyPyFile:
        # fy:end <<<===

        flow_name = PythonEntityName.from_pascal_case(self._flow_file_split.flow_name)

        parsed_fy_py_file = ParsedFlowFyPyFile(
            pre_fy_code=self._pre_fy_code,
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._flow_file_split.user_imports,
            flow_name=flow_name,
            generics_def=self._flow_file_split.generics_def,
            declared_base_flow=self._flow_file_split.declared_base_flow,
            return_type=self._flow_file_split.return_type,
            properties=self._included_mixins.property_mixins,
            methods=self._included_mixins.method_mixins,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{flow_name.pascal_case}_Flow"
            ),
            # TODO: remove after removed from the base class.
            template_model=TemporaryBaseTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{flow_name.pascal_case}_Flow"
                ),
                entity_key_value=flow_name.snake_case,
            ),
        )

        return parsed_fy_py_file
