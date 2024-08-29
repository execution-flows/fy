"""fy
from domain.parsed_fy_py_file import ParsedFlowFyPyFile


property parsed_flow_fy_py_file: ParsedFlowFyPyFile using parsed_fy_py_file:
    property fy_code
    property pre_marker_file_content
    property post_marker_file_content
    property fy_py_file_to_parse
    property flow_file_split
    property property_mixins
    property method_mixins
"""

from domain.fy_py_template_models import FlowTemplateModel
from domain.parsed_fy_py_file import ParsedFlowFyPyFile
from functools import cached_property

from domain.python_entity_name import PythonEntityName
from mixins.property.flow_file_split.abc_fy import (
    With_FlowFileSplit_PropertyMixin_ABC,
)
from mixins.property.fy_code.abc_fy import (
    With_FyCode_PropertyMixin_ABC,
)
from mixins.property.fy_py_file_to_parse.abc_fy import (
    With_FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.method_mixins.abc_fy import (
    With_MethodMixins_PropertyMixin_ABC,
)
from mixins.property.post_marker_file_content.abc_fy import (
    With_PostMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.pre_marker_file_content.abc_fy import (
    With_PreMarkerFileContent_PropertyMixin_ABC,
)
from mixins.property.property_mixins.abc_fy import (
    With_PropertyMixins_PropertyMixin_ABC,
)
import abc


# fy:start ===>>>
class ParsedFlowFyPyFile_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    With_FyCode_PropertyMixin_ABC,
    With_PreMarkerFileContent_PropertyMixin_ABC,
    With_PostMarkerFileContent_PropertyMixin_ABC,
    With_FyPyFileToParse_PropertyMixin_ABC,
    With_FlowFileSplit_PropertyMixin_ABC,
    With_PropertyMixins_PropertyMixin_ABC,
    With_MethodMixins_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_flow_fy_py_file(self) -> ParsedFlowFyPyFile:
        # fy:end <<<===

        flow_name = PythonEntityName.from_pascal_case(self._flow_file_split.flow_name)

        parsed_fy_py_file = ParsedFlowFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=self._flow_file_split.user_imports,
            template_model=FlowTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{flow_name.pascal_case}_Flow"
                ),
                flow_name=flow_name,
                return_type=self._flow_file_split.return_type,
                properties=self._property_mixins,
                methods=self._method_mixins,
            ),
        )

        return parsed_fy_py_file
