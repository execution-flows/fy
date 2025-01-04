# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
property property_impl_1: str using impl_1:
    property property_required_1
    property property_required_2
fy"""

import abc
from functools import cached_property
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property1.abc_fy import (
    PropertyRequired1_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property2.abc_fy import (
    PropertyRequired2_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.ordered_abstract_entities_test.property3.abc_fy import (
    PropertyImpl1_PropertyMixin_ABC,
)


# fy:start ===>>>
class PropertyImpl1_UsingImpl1_PropertyMixin(
    # Property Mixins
    PropertyImpl1_PropertyMixin_ABC,
    PropertyRequired1_PropertyMixin_ABC,
    PropertyRequired2_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _property_impl_1(self) -> str:
        # fy:end <<<===
        return self._property_required_1 + self._property_required_2
