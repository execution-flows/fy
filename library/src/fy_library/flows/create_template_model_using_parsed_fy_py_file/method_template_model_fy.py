# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreateMethodTemplateModel_UsingParsedFyPyFile -> MethodTemplateModel:
    property parsed_fy_py_file using setter
    property abstract_entities_ordering_index using setter
    property abstract_mixins using parsed_method_fy_py_file
    property mro_ordered_abstract_mixins using abstract_mixins_and_ordered_abstract_entities
"""

from typing import Any, Dict, List

from fy_core.base.flow_base import FlowBase

from fy_library.domain.fy_py_template_models import MethodTemplateModel
from fy_library.domain.mixin_models import BaseMixinModel, MixinModelKind
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedMethodFyPyFile,
)
from fy_library.mixins.property.abstract_mixins.using_parsed_method_fy_py_file_with_filtered_method_mixins_fy import (
    AbstractMixins_UsingParsedMethodFyPyFile_PropertyMixin,
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


# fy:start ===>>>
class CreateMethodTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
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
        abstract_entities_ordering_index: Dict[str, int],
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        self._abstract_entities_ordering_index = abstract_entities_ordering_index
        super().__init__(*args, **kwargs)

    def __call__(self) -> MethodTemplateModel:
        # fy:end <<<===
        parsed_method_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_method_fy_py_file, ParsedMethodFyPyFile)

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

        return MethodTemplateModel(
            python_class_name=parsed_method_fy_py_file.python_class_name,
            method_name=parsed_method_fy_py_file.method_name,
            abstract_method_mixins=abstract_method_mixins,
            abstract_property_mixins=abstract_property_mixins,
            generics_def=parsed_method_fy_py_file.generics_def,
            arguments=parsed_method_fy_py_file.arguments,
            implementation_name=parsed_method_fy_py_file.implementation_name,
            return_type=parsed_method_fy_py_file.return_type,
        )
