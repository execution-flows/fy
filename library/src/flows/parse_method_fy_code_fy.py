"""fy
from domain.parsed_fy_py_file import ParsedFyPyFile


flow ParseMethodFyCode -> ParsedFyPyFile:
    property fy_code using setter
    property pre_marker_file_content using setter
    property post_marker_file_content using setter
    property fy_py_file_to_parse using setter
    property method_file_split using method_regex
    property declared_abstract_property_mixins using mixin_lines
    property declared_abstract_method_mixins using mixin_lines
"""

from pathlib import Path
from typing import Any

from base.flow_base import FlowBase
from domain.fy_py_template_models import (
    MethodTemplateModel,
)
from domain.parsed_fy_py_file import ParsedFyPyFile, ParsedMethodFyPyFile
from domain.python_entity_name import PythonEntityName
from mixins.property.declared_abstract_method_mixins.using_mixin_lines_fy import (
    DeclaredAbstractMethodMixins_UsingMixinLines_PropertyMixin,
)
from mixins.property.declared_abstract_property_mixins.using_mixin_lines_fy import (
    DeclaredAbstractPropertyMixins_UsingMixinLines_PropertyMixin,
)
from mixins.property.fy_code.using_setter import (
    FyCode_UsingSetter_PropertyMixin,
)
from mixins.property.fy_py_file_to_parse.using_setter import (
    FyPyFileToParse_UsingSetter_PropertyMixin,
)
from mixins.property.method_file_split.using_method_regex_fy import (
    MethodFileSplit_UsingMethodRegex_PropertyMixin,
)
from mixins.property.post_marker_file_content.using_setter import (
    PostMarkerFileContent_UsingSetter_PropertyMixin,
)
from mixins.property.pre_marker_file_content.using_setter import (
    PreMarkerFileContent_UsingSetter_PropertyMixin,
)


# fy:start <<<===
class ParseMethodFyCode_Flow(
    # Property Mixins
    FyCode_UsingSetter_PropertyMixin,
    PreMarkerFileContent_UsingSetter_PropertyMixin,
    PostMarkerFileContent_UsingSetter_PropertyMixin,
    FyPyFileToParse_UsingSetter_PropertyMixin,
    MethodFileSplit_UsingMethodRegex_PropertyMixin,
    DeclaredAbstractPropertyMixins_UsingMixinLines_PropertyMixin,
    DeclaredAbstractMethodMixins_UsingMixinLines_PropertyMixin,
    # Base
    FlowBase[ParsedFyPyFile],
):
    def __call__(self) -> ParsedFyPyFile:
        # fy:end <<<===
        user_imports = self._method_file_split[0]
        method_name = PythonEntityName.from_snake_case(self._method_file_split[1])
        arguments = self._method_file_split[3]
        return_type = self._method_file_split[4]
        implementation_name = PythonEntityName.from_snake_case(
            self._method_file_split[5]
        )

        parsed_fy_py_file = ParsedMethodFyPyFile(
            fy_code=self._fy_code,
            pre_marker_file_content=self._pre_marker_file_content,
            post_marker_file_content=self._post_marker_file_content,
            file_path=self._fy_py_file_to_parse,
            user_imports=user_imports,
            template_model=MethodTemplateModel(
                python_class_name=PythonEntityName.from_pascal_case(
                    f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
                ),
                method_name=method_name,
                implementation_name=implementation_name,
                abstract_property_mixins=self._declared_abstract_property_mixins,
                abstract_method_mixins=self._declared_abstract_method_mixins,
                arguments=arguments,
                return_type=return_type,
            ),
        )
        return parsed_fy_py_file

    def __init__(
        self,
        *args: Any,
        fy_code: str,
        pre_marker_file_content: str,
        post_marker_file_content: str,
        fy_py_file_to_parse: Path,
        **kwargs: Any,
    ):
        self._fy_code = fy_code
        self._fy_py_file_to_parse = fy_py_file_to_parse
        self._pre_marker_file_content = pre_marker_file_content
        self._post_marker_file_content = post_marker_file_content
        super().__init__(*args, **kwargs)
