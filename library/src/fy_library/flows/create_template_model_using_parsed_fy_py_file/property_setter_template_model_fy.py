# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
flow create_property_setter_template_model__using_parsed_fy_py_file -> PropertySetterTemplateModel:
    property parsed_fy_py_file using setter
    property parsed_fy_py_files_map_by_key using setter
fy"""

from typing import Any, cast

from fy_core.base.flow_base import FlowBase
from fy_library.domain.fy_py_template_models import PropertySetterTemplateModel
from fy_library.domain.mixin_models import AbstractPropertyModel, MixinModelKind
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    PropertySetterFyPyFile,
    ParsedAbstractPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_file.using_setter import (
    ParsedFyPyFile_UsingSetter_PropertyMixin,
)


# fy:start ===>>>
class CreatePropertySetterTemplateModel_UsingParsedFyPyFile_Flow(
    # Property Mixins
    ParsedFyPyFile_UsingSetter_PropertyMixin,
    # Base
    FlowBase[PropertySetterTemplateModel],
):
    def __init__(
        self,
        *args: Any,
        parsed_fy_py_file: ParsedFyPyFile,
        **kwargs: Any,
    ):
        self._parsed_fy_py_file = parsed_fy_py_file
        super().__init__(*args, **kwargs)

    def __call__(self) -> PropertySetterTemplateModel:
        # fy:end <<<===
        parsed_property_setter_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_property_setter_fy_py_file, PropertySetterFyPyFile)
        own_property_setter_entity_key = (
            ParsedFyPyFileKind.ABSTRACT_PROPERTY,
            parsed_property_setter_fy_py_file.property_name.snake_case,
        )

        parsed_abstract_property_fy_py_file = cast(
            ParsedAbstractPropertyFyPyFile,
            self._parsed_fy_py_files_map_by_key[own_property_setter_entity_key],
        )
        return PropertySetterTemplateModel(
            python_class_name=parsed_property_setter_fy_py_file.python_class_name,
            property_name=parsed_property_setter_fy_py_file.property_name,
            property_type=parsed_property_setter_fy_py_file.property_type,
            generics_def=parsed_property_setter_fy_py_file.generics_def,
            own_abstract_property_mixin=AbstractPropertyModel(
                python_class_name=parsed_abstract_property_fy_py_file.python_class_name,
                kind=MixinModelKind.ABSTRACT_PROPERTY,
                property_name=parsed_property_setter_fy_py_file.property_name,
                generics_impl=(
                    parsed_property_setter_fy_py_file.generics_def
                    or parsed_property_setter_fy_py_file.property_type
                )
                if parsed_abstract_property_fy_py_file.generics_def != ""
                else "",
            ),
        )
