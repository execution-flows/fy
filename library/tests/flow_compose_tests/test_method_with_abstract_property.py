# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from flow_compose_tests.test_utils.main_flow_compose_test_case import (
    MainFlowComposeTestCase,
)


class TestMethodWithAbstractProperty(MainFlowComposeTestCase):
    def test_method_with_abstract_property(self) -> None:
        self._test_main_flow(target_folder="method_with_abstract_property")
