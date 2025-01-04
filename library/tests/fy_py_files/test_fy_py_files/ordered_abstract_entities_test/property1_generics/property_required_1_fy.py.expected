# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_required_1_generics: str using required_1:
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property1_generics.abc_fy import (
    PropertyRequired1Generics_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyRequired1Generics_UsingRequired1_PropertyMixin(
    # Property Mixins
    PropertyRequired1Generics_PropertyMixin_ABC[str],
    abc.ABC,
):
    @cached_property
    def _property_required_1_generics(self) -> str:
        # fy:end <<<===
        return "required_1"
