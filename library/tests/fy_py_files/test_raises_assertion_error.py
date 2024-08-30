# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestRaisesAssertionError(MainFyPyTestCase):
    def test_raises_assertion_error_flow_invalid_mixin(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Flow .*/assert_flow_fy.py cannot include other abstract property implementations",
        ):
            self._test_main_flow(
                target_folder="raises_assertion_error/flow_invalid_mixin"
            )

    def test_raises_assertion_error_method_invalid_abstract_mixins(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Method .*/assert_method_fy.py cannot include other method implementations",
        ):
            self._test_main_flow(
                target_folder="raises_assertion_error/method_invalid_abstract_mixins"
            )

    def test_raises_assertion_error_property_invalid_abstract_mixins(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Property .*/assert_property_fy.py cannot include other property implementations",
        ):
            self._test_main_flow(
                target_folder="raises_assertion_error/property_invalid_abstract_mixins"
            )
