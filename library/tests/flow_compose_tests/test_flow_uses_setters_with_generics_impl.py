# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from flow_compose_tests.test_utils.main_flow_compose_test_case import (
    MainFlowComposeTestCase,
)


class TestFlowUsesSettersWithGenericsImpl(MainFlowComposeTestCase):
    def test_flow_uses_setters_with_generics_impl(self) -> None:
        self._test_main_flow(target_folder="flow_uses_setters_with_generics_impl")
