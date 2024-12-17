# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestRaisesAssertionError(MainFyPyTestCase):
    def test_invalid_annotation_placement_raises_error(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Base flow has unordered annotations in HelloError_BaseFlow.",
        ):
            self._test_main_flow(
                target_folder="unordered_annotation_raises_error",
                perform_fy_code_deletion=False,
            )
