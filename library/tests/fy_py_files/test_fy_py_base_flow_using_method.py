# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestRaisesAssertionError(MainFyPyTestCase):
    def test_base_flow_using_method_assert(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Base flow .*/hello_world_using_method_fy.py cannot include method implementations.",
        ):
            self._test_main_flow(
                target_folder="base_flow_using_method_assert",
                perform_fy_code_deletion=False,
            )
