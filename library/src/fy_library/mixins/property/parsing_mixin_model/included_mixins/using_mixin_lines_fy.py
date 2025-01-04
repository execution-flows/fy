# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.mixins.property.parsing_mixin_model.included_mixins.abc_fy import IncludedMixinsModel


property included_mixins: IncludedMixinsModel using mixin_models:
    property mixin_models
fy"""

import abc
from functools import cached_property


from fy_library.domain.mixin_models import MixinModelKind, BaseMixinModel
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsing_mixin_model.included_mixins.abc_fy import (
    IncludedMixins_PropertyMixin_ABC,
    IncludedMixinsModel,
)
from fy_library.mixins.property.parsing_mixin_model.mixin_models.abc_fy import (
    MixinModels_PropertyMixin_ABC,
)


# fy:start ===>>>
class IncludedMixins_UsingMixinModels_PropertyMixin(
    # Property Mixins
    IncludedMixins_PropertyMixin_ABC,
    MixinModels_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _included_mixins(self) -> IncludedMixinsModel:
        # fy:end <<<===
        check_for_duplicates_dict: dict[
            tuple[ParsedFyPyFileKind, str], BaseMixinModel
        ] = {}
        for mixin_model in self._mixin_models:
            if mixin_model.entity_key in check_for_duplicates_dict:
                raise AssertionError(
                    f"Duplicate found in {mixin_model.entity_key, mixin_model.kind.name}."
                )
            check_for_duplicates_dict[mixin_model.entity_key] = mixin_model

        included_mixins = IncludedMixinsModel(
            abstract_method_mixins=[
                mixin_model
                for mixin_model in self._mixin_models
                if mixin_model.kind == MixinModelKind.ABSTRACT_METHOD
            ],
            abstract_property_mixins=[
                mixin_model
                for mixin_model in self._mixin_models
                if mixin_model.kind == MixinModelKind.ABSTRACT_PROPERTY
            ],
            method_mixins=[
                mixin_model
                for mixin_model in self._mixin_models
                if mixin_model.kind == MixinModelKind.METHOD
            ],
            property_mixins=[
                mixin_model
                for mixin_model in self._mixin_models
                if mixin_model.kind == MixinModelKind.PROPERTY
            ],
        )

        return included_mixins
