# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel


property template_model: BaseTemplateModel using parsed_fy_py_file:
    property parsed_fy_py_file
    property parsed_fy_py_files_map_by_key
"""

import abc
from functools import cached_property

from fy_library.constants import PROPERTY_SETTER_IMPLEMENTATION_NAME
from fy_library.domain.fy_py_template_models import (
    BaseTemplateModel,
    FlowTemplateModelWithPropertySetters,
    FlowTemplateModel,
    BaseFlowTemplateModel,
    BaseFlowTemplateModelWithPropertySetters,
)
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)


# fy:start ===>>>
class TemplateModel_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    ParsedFyPyFile_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _template_model(self) -> BaseTemplateModel:
        # fy:end <<<===
        match self._parsed_fy_py_file.file_type:
            case ParsedFyPyFileKind.FLOW:
                return self.__flow_template()
            case ParsedFyPyFileKind.BASE_FLOW:
                return self.__base_flow_template()
            case _:
                return self._parsed_fy_py_file.template_model

    def __flow_template(self) -> FlowTemplateModel:
        assert isinstance(self._parsed_fy_py_file.template_model, FlowTemplateModel)

        property_setters = [
            self._parsed_fy_py_files_map_by_key[
                property_setter.property_name.snake_case
            ].template_model
            for property_setter in self._parsed_fy_py_file.template_model.properties
            if property_setter.implementation_name.snake_case
            == PROPERTY_SETTER_IMPLEMENTATION_NAME
        ]

        return FlowTemplateModelWithPropertySetters.model_validate(
            {
                **self._parsed_fy_py_file.template_model.model_dump(),
                "property_setters": property_setters,
            }
        )

    def __base_flow_template(self) -> BaseFlowTemplateModel:
        assert isinstance(self._parsed_fy_py_file.template_model, BaseFlowTemplateModel)

        property_setters = [
            self._parsed_fy_py_files_map_by_key[
                property_setter.property_name.snake_case
            ].template_model
            for property_setter in self._parsed_fy_py_file.template_model.properties
            if property_setter.implementation_name.snake_case
            == PROPERTY_SETTER_IMPLEMENTATION_NAME
        ]

        return BaseFlowTemplateModelWithPropertySetters.model_validate(
            {
                **self._parsed_fy_py_file.template_model.model_dump(),
                "property_setters": property_setters,
            }
        )
