# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_file_split: PropertyFileSplitModel using property_regex:
    property fy_code
"""

import abc
import re
from functools import cached_property
from typing import Final

from fy_library.constants import (
    FY_ENTITY_REGEX_STRING,
    PYTHON_MULTI_ENTITY_REGEX_STRING,
)
from fy_library.mixins.property.property_file_split.abc_fy import (
    PropertyFileSplitModel,
    PropertyFileSplit_PropertyMixin_ABC,
)

from fy_library.mixins.property.fy_code.abc_fy import (
    FyCode_PropertyMixin_ABC,
)

_PROPERTY_REGEX: Final = re.compile(
    rf"property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})"
    rf"\s*(?:\[(?P<generics>{PYTHON_MULTI_ENTITY_REGEX_STRING})])?"
    rf"\s*:\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
)


# fy:start ===>>>
class PropertyFileSplit_UsingPropertyRegex_PropertyMixin(
    # Property_mixins
    FyCode_PropertyMixin_ABC,
    PropertyFileSplit_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_file_split(self) -> PropertyFileSplitModel:
        # fy:end <<<===
        property_file_split = _PROPERTY_REGEX.split(self._fy_code)

        assert (
            len(property_file_split) == 6
        ), f"Property file split length {len(property_file_split)} is invalid"

        property_file_split_model = PropertyFileSplitModel(
            user_imports=property_file_split[0],
            property_name=property_file_split[1],
            implementation_name=property_file_split[4],
            generics_def=property_file_split[2] or "",
            property_type=property_file_split[3] or "",
            mixins=property_file_split[5],
        )

        return property_file_split_model
