# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from test_utils.main_flow_text_case import MainFlowTestCase


class TestHelloIntegerFy(MainFlowTestCase):
    def test_hello_integer_generates_file(self) -> None:
        self._test_main_flow(target_folder="hello_integer")
