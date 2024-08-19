# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from fy_files.test_utils.main_flow_text_case import MainFlowTestCase


class TestFlowUsingMethodAndPropertyMixinsFy(MainFlowTestCase):
    def test_flow_using_method_and_property_mixins(self) -> None:
        self._test_main_flow(target_folder="flow_using_method_and_property_mixins")
