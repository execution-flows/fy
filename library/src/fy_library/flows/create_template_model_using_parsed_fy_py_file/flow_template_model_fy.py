# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import FlowTemplateModel


flow create_flow_template_model__using_parsed_fy_py_file_and_property_setters_template_models -> FlowTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
    property property_mixins using template_model_properties
    property property_setter_mixins using property_mixins
    property property_constant_setter_mixins using property_mixins
    property parsed_fy_py_files using property_setter_mixins__mapped_to_abstract_property
fy"""

from typing import Any, cast

from fy_core.base.flow_base import FlowBase

from fy_library.domain.fy_py_template_models import (
    FlowTemplateModel,
)
from fy_library.domain.mixin_models import PropertyMixinModel, MethodMixinModel
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedFlowFyPyFile,
    ParsedAbstractPropertyFyPyFile,
    ParsedMethodFyPyFile,
    ParsedPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.entity_mixins.property_mixins.using_template_model_properties_fy import (
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files.using_property_setter_mixins__mapped_to_abstract_property__fy import (
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_setters.property_constant_setter_mixins.using_property_mixins_fy import (
    PropertyConstantSetterMixins_UsingPropertyMixins_PropertyMixin,
)
from fy_library.mixins.property.property_setters.property_setter_mixins.using_property_mixin_fy import (
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
)


# fy:start ===>>>
class CreateFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    PropertyConstantSetterMixins_UsingPropertyMixins_PropertyMixin,
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
    # Base
    FlowBase[FlowTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        super().__init__(*args, **kwargs)

    def __call__(self) -> FlowTemplateModel:
        # fy:end <<<===
        parsed_flow_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_flow_fy_py_file, ParsedFlowFyPyFile)
        declared_base_flow = PythonEntityName.from_snake_case(
            parsed_flow_fy_py_file.declared_base_flow
        )
        property_setters_names: set[str] = {
            cast(ParsedAbstractPropertyFyPyFile, p).abstract_property_name.snake_case
            for p in self._parsed_fy_py_files
        }.union(
            {p.property_name.snake_case for p in self._property_constant_setter_mixins}
        )

        def get_property_type(prop: PropertyMixinModel) -> str:
            if prop.entity_key in self._parsed_fy_py_files_map_by_key:
                return cast(
                    ParsedPropertyFyPyFile,
                    self._parsed_fy_py_files_map_by_key[prop.entity_key],
                ).property_type
            abstract_prop = cast(
                ParsedAbstractPropertyFyPyFile,
                self._parsed_fy_py_files_map_by_key[
                    (
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        prop.property_name.snake_case,
                    )
                ],
            )
            if abstract_prop.generics_def:
                return prop.generics_impl
            return abstract_prop.property_type

        property_mixins: list[PropertyMixinModel] = [
            PropertyMixinModel(
                **prop.model_dump(exclude={"property_type"}),
                property_type=get_property_type(prop),
            )
            for prop in parsed_flow_fy_py_file.properties
        ]

        property_constant_setters: list[PropertyMixinModel] = [
            PropertyMixinModel(
                **prop.model_dump(exclude={"property_type"}),
                property_type=get_property_type(prop),
            )
            for prop in self._property_constant_setter_mixins
        ]

        method_mixins: list[MethodMixinModel] = [
            MethodMixinModel(
                **method.model_dump(exclude={"return_type"}),
                return_type=cast(
                    ParsedMethodFyPyFile,
                    self._parsed_fy_py_files_map_by_key[method.entity_key],
                ).return_type,
            )
            for method in parsed_flow_fy_py_file.methods
        ]

        property_mixins_in_use: list[PropertyMixinModel] = [
            property
            for property in property_mixins
            if f"self._{property.property_name.snake_case}"
            in self._parsed_fy_py_file.post_marker_file_content
        ]
        method_mixins_in_use: list[MethodMixinModel] = [
            method
            for method in method_mixins
            if f"self._{method.method_name.snake_case}"
            in self._parsed_fy_py_file.post_marker_file_content
        ]

        return FlowTemplateModel(
            python_class_name=parsed_flow_fy_py_file.python_class_name,
            flow_name=parsed_flow_fy_py_file.flow_name,
            generics_def=parsed_flow_fy_py_file.generics_def,
            declared_base_flow=PythonEntityName.from_pascal_case(
                f"{declared_base_flow.pascal_case}_BaseFlow"
            )
            if parsed_flow_fy_py_file.declared_base_flow != ""
            else None,
            declared_base_flow_generics_def=parsed_flow_fy_py_file.declared_base_flow_generics_def,
            return_type=parsed_flow_fy_py_file.return_type,
            properties=property_mixins,
            properties_without_setters=[
                p
                for p in parsed_flow_fy_py_file.properties
                if p.property_name.snake_case not in property_setters_names
            ],
            methods=method_mixins,
            property_setters=self._parsed_fy_py_files,
            property_constant_setters=property_constant_setters,
            property_mixins_in_use=property_mixins_in_use,
            method_mixins_in_use=method_mixins_in_use,
        )
