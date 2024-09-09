# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestBaseFlowWithAbcMethodFyPyGeneratesFile(MainFyPyTestCase):
    def test_fy_py_base_flow_with_abc_method(self) -> None:
        self._test_main_flow(target_folder="base_flow_with_abc_method")