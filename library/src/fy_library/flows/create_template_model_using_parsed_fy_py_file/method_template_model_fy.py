# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow create_method_template_model__using_parsed_fy_py_file -> MethodTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
    property abstract_entities_ordering_index using setter
    property abstract_mixins using parsed_method_fy_py_file
    property mro_ordered_abstract_mixins using abstract_mixins_and_ordered_abstract_entities
fy"""

from typing import Any, List, cast

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import MethodTemplateModel
from fy_library.domain.mixin_models import (
    MixinModelKind,
    AbstractPropertyModel,
    AbstractMethodModel,
)
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedMethodFyPyFile,
    ParsedAbstractPropertyFyPyFile,
    ParsedAbstractMethodFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.entity_mixins.abstract_mixins.using_parsed_method_fy_py_file_with_filtered_method_mixins_fy import (
    AbstractMixins_UsingParsedMethodFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.mro.mro_ordered_abstract_mixins.new_parsed_fy_py_file_and_ordered_abstract_entities_fy import (
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
)
from fy_library.mixins.property.mro.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.using_setter import (
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreateMethodTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    ParsedFyPyFilesMapByKey_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    AbstractMixins_UsingParsedMethodFyPyFile_PropertyMixin,
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
    # Base
    FlowBase[MethodTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        parsed_fy_py_files_map_by_key: dict[
            tuple[ParsedFyPyFileKind, str], ParsedFyPyFile
        ],
        abstract_entities_ordering_index: dict[tuple[ParsedFyPyFileKind, str], int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._parsed_fy_py_files_map_by_key = parsed_fy_py_files_map_by_key
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> MethodTemplateModel:
        # fy:end <<<===
        parsed_method_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_method_fy_py_file, ParsedMethodFyPyFile)

        abstract_method_mixins: List[AbstractMethodModel] = [
            AbstractMethodModel(
                **abstract_property.model_dump(exclude={"return_type"}),
                return_type=cast(
                    ParsedAbstractMethodFyPyFile,
                    self._parsed_fy_py_files_map_by_key[abstract_property.entity_key],
                ).return_type,
            )
            for abstract_property in self._mro_ordered_abstract_mixins
            if abstract_property.kind == MixinModelKind.ABSTRACT_METHOD
        ]

        def get_property_type(prop: AbstractPropertyModel) -> str:
            abstract_prop = cast(
                ParsedAbstractPropertyFyPyFile,
                self._parsed_fy_py_files_map_by_key[prop.entity_key],
            )
            if abstract_prop.generics_def:
                return prop.generics_impl
            return abstract_prop.property_type

        abstract_property_mixins: List[AbstractPropertyModel] = [
            AbstractPropertyModel(
                **abstract_property.model_dump(exclude={"property_type"}),
                property_type=get_property_type(
                    cast(AbstractPropertyModel, abstract_property)
                ),
            )
            for abstract_property in self._mro_ordered_abstract_mixins
            if abstract_property.kind == MixinModelKind.ABSTRACT_PROPERTY
        ]

        template_model = MethodTemplateModel(
            python_class_name=parsed_method_fy_py_file.python_class_name,
            method_name=parsed_method_fy_py_file.method_name,
            abstract_method_non_generic_mixins=[
                m for m in abstract_method_mixins if m.generics_impl == ""
            ],
            abstract_method_generic_mixins=[
                m for m in abstract_method_mixins if m.generics_impl != ""
            ],
            abstract_property_non_generic_mixins=[
                m for m in abstract_property_mixins if m.generics_impl == ""
            ],
            abstract_property_generic_mixins=[
                m for m in abstract_property_mixins if m.generics_impl != ""
            ],
            generics_def=parsed_method_fy_py_file.generics_def,
            arguments=parsed_method_fy_py_file.arguments,
            implementation_name=parsed_method_fy_py_file.implementation_name,
            return_type=parsed_method_fy_py_file.return_type,
        )
        return template_model
