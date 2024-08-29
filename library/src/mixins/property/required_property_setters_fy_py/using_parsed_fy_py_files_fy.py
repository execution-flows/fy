"""fy
from typing import List
from domain.parsed_fy_py_file import ParsedFyPyFile


@cached
property required_property_setters_fy_py: List[ParsedFyPyFile] using parsed_fy_py_files:
    property parsed_fy_py_files
    property parsed_fy_py_files_map_by_key
"""

import abc
from functools import cached_property
from typing import List, cast

from domain.fy_py_template_models import (
    PropertySetterTemplateModel,
    AbstractPropertyTemplateModel,
)
from domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    PropertySetterFyPyFile,
    ParsedFyPyFileKind,
    ParsedFlowFyPyFile,
)
from domain.python_entity_name import PythonEntityName
from mixins.property.parsed_fy_py_files.abc_fy import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    With_ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class RequiredPropertySettersFyPy_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    With_ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _required_property_setters_fy_py(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        required_setters = {
            flow_property.property_name.snake_case: PropertySetterFyPyFile(
                fy_code="",
                pre_marker_file_content="",
                post_marker_file_content="",
                file_path=self._parsed_fy_py_files_map_by_key[
                    flow_property.property_name.snake_case
                ].file_path.with_name("using_setter.py"),
                user_imports=self._parsed_fy_py_files_map_by_key[
                    flow_property.property_name.snake_case
                ].user_imports,
                template_model=PropertySetterTemplateModel(
                    property_name=flow_property.property_name,
                    python_class_name=PythonEntityName.from_pascal_case(
                        f"{flow_property.property_name.pascal_case}_UsingSetter_PropertyMixin"
                    ),
                    property_type=cast(
                        AbstractPropertyTemplateModel,
                        self._parsed_fy_py_files_map_by_key[
                            flow_property.property_name.snake_case
                        ].template_model,
                    ).property_type,
                ),
            )
            for parsed_fy_py_file in self._parsed_fy_py_files
            if parsed_fy_py_file.file_type == ParsedFyPyFileKind.FLOW
            for flow_property in cast(
                ParsedFlowFyPyFile, parsed_fy_py_file
            ).template_model.properties
            if (
                flow_property.implementation_name.snake_case == "setter"
                and f"{flow_property.property_name.snake_case}.setter"
                not in self._parsed_fy_py_files_map_by_key
            )
        }

        return list(required_setters.values())
