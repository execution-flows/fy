# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow CreatePropertyTemplateModel_UsingParsedFyPyFile -> PropertyTemplateModel:
    property parsed_fy_py_file using setter
    property abstract_entities_ordering_index using setter
    property abstract_mixins using parsed_property_fy_py_file
    property mro_ordered_abstract_mixins using abstract_mixins_and_ordered_abstract_entities
"""

from typing import Any, Dict

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import PropertyTemplateModel
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile, ParsedPropertyFyPyFile
from fy_library.mixins.property.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)

from fy_library.mixins.property.abstract_mixins.using_parsed_property_fy_py_file_fy import (
    AbstractMixins_UsingParsedPropertyFyPyFile_PropertyMixin,
)
from fy_library.mixins.property.mro_ordered_abstract_mixins.new_parsed_fy_py_file_and_ordered_abstract_entities_fy import (
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
)

from fy_library.mixins.property.ordered_abstract_entities.using_setter import (
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreatePropertyTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    AbstractEntitiesOrderingIndex_UsingSetter_PropertyMixin,
    AbstractMixins_UsingParsedPropertyFyPyFile_PropertyMixin,
    MroOrderedAbstractMixins_UsingAbstractMixinsAndOrderedAbstractEntities_PropertyMixin,
    # Base
    FlowBase[PropertyTemplateModel],
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

    def __call__(self) -> PropertyTemplateModel:
        # fy:end <<<===
        parsed_property_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_property_fy_py_file, ParsedPropertyFyPyFile)
        return PropertyTemplateModel(
            python_class_name=parsed_property_fy_py_file.python_class_name,
            property_name=parsed_property_fy_py_file.property_name,
            implementation_name=parsed_property_fy_py_file.implementation_name,
            abstract_property_mixins=self._mro_ordered_abstract_mixins,
            generics_def=parsed_property_fy_py_file.generics_def,
            property_type=parsed_property_fy_py_file.property_type,
        )
