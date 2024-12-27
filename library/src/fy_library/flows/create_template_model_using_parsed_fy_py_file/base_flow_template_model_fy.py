# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseFlowTemplateModel


flow CreateBaseFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels -> BaseFlowTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
    property property_mixins using template_model_properties
    property property_setter_mixins using property_mixins
    property parsed_fy_py_files using property_setter_mixins__mapped_to_abstract_property
    property abstract_entities_ordering_index using setter
    property abstract_mixins using parsed_base_flow_fy_py_file
    property mro_ordered_abstract_mixins using abstract_mixins_and_ordered_abstract_entities
"""

from typing import Any, List
from typing import Dict

from fy_core.base.flow_base import FlowBase

from fy_library.domain.fy_py_template_models import (
    BaseFlowTemplateModel,
)
from fy_library.domain.mixin_models import BaseMixinModel, MixinModelKind
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedBaseFlowFyPyFile,
)
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.abstract_mixins.using_parsed_base_flow_fy_py_file_fy import (
    AbstractMixins_UsingParsedBaseFlowFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.mro_ordered_abstract_mixins.new_parsed_fy_py_file_and_ordered_abstract_entities_fy import (
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
)
from fy_library.mixins.property.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files.using_property_setter_mixins__mapped_to_abstract_property__fy import (
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.property_mixins.using_template_model_properties_fy import (
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
)
from fy_library.mixins.property.property_setter_mixins.using_property_mixin_fy import (
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
)


# fy:start ===>>>
class CreateBaseFlowTemplateModel_UsingParsedFyPyFileAndPropertySettersTemplateModels_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    PropertyMixins_UsingTemplateModelProperties_PropertyMixin,
    PropertySetterMixins_UsingPropertyMixins_PropertyMixin,
    ParsedFyPyFiles_UsingPropertySetterMixins_MappedToAbstractProperty_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    AbstractMixins_UsingParsedBaseFlowFyPyFile_PropertyMixin,
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
    # Base
    FlowBase[BaseFlowTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        parsed_fy_py_files_map_by_key: Dict[str, ParsedFyPyFile],
        abstract_entities_ordering_index: Dict[str, int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> BaseFlowTemplateModel:
        # fy:end <<<===
        parsed_base_flow_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_base_flow_fy_py_file, ParsedBaseFlowFyPyFile)

        callable_annotation = any(
            "@callable" == annotation.name
            for annotation in parsed_base_flow_fy_py_file.annotations
        )

        abstract_method_mixins: List[BaseMixinModel] = [
            abstract_property
            for abstract_property in self._mro_ordered_abstract_mixins
            if abstract_property.kind == MixinModelKind.ABSTRACT_METHOD
        ]
        abstract_property_mixins: List[BaseMixinModel] = [
            abstract_method
            for abstract_method in self._mro_ordered_abstract_mixins
            if abstract_method.kind == MixinModelKind.ABSTRACT_PROPERTY
        ]

        return BaseFlowTemplateModel(
            python_class_name=parsed_base_flow_fy_py_file.python_class_name,
            base_flow_name=parsed_base_flow_fy_py_file.base_flow_name,
            generics_def=parsed_base_flow_fy_py_file.generics_def,
            declared_base_flow=PythonEntityName.from_pascal_case(
                f"{parsed_base_flow_fy_py_file.declared_base_flow}_BaseFlow"
            )
            if parsed_base_flow_fy_py_file.declared_base_flow != ""
            else None,
            callable_annotation=callable_annotation,
            return_type=parsed_base_flow_fy_py_file.return_type,
            properties=parsed_base_flow_fy_py_file.properties,
            methods=parsed_base_flow_fy_py_file.methods,
            abstract_property_mixins=abstract_property_mixins,
            abstract_method_mixins=abstract_method_mixins,
            property_setters=self._parsed_fy_py_files,
        )
