# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from tests.fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestFyPyMainFlowTest(MainFyPyTestCase):
    def test_run_fy_py_main_flow_test(self) -> None:
        self._run_fy_py_main_flow(target_folder="flow_using_method_and_property_mixins")
