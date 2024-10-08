# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestRaisesAssertionError(MainFyPyTestCase):
    def test_flow_invalid_mixin_raises_correct_error(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Flow .*/flow_invalid_mixin_fy.py cannot include other abstract property implementations",
        ):
            self._test_main_flow(
                target_folder="invalid_fy_code_raises_correct_error/flow_invalid_mixin",
                perform_fy_code_deletion=False,
            )

    def test_method_invalid_abstract_mixins_raises_correct_error(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=r"Method .*/method_invalid_abstract_mixin_fy.py cannot include other method implementations",
        ):
            self._test_main_flow(
                target_folder="invalid_fy_code_raises_correct_error/method_invalid_abstract_mixins",
                perform_fy_code_deletion=False,
            )

    def test_property_invalid_abstract_mixins_raises_correct_error(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex=(
                r"Property .*/property_invalid_abstract_mixin_fy.py "
                r"cannot include other method implementations"
            ),
        ):
            self._test_main_flow(
                target_folder="invalid_fy_code_raises_correct_error/property_invalid_abstract_mixins",
                perform_fy_code_deletion=False,
            )

    def test_property_raises_correct_error(self) -> None:
        with self.assertRaisesRegex(
            expected_exception=ValueError,
            expected_regex=r"Line\s+prop erty french_greeting in .*/property_invalid_keyword_fy.py is invalid.",
        ):
            self._test_main_flow(
                target_folder="invalid_fy_code_raises_correct_error/property_invalid_mixin_keyword",
                perform_fy_code_deletion=False,
            )
