# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from fy_py_files.test_utils.main_fypy_test_case import MainFyPyTestCase


class TestAbstractMethodFyPyWithGenericsWithoutReturnTypeRaisesError(MainFyPyTestCase):
    def test_fy_py_abstract_method_with_generics_without_return_type_raises_error(
        self,
    ) -> None:
        with self.assertRaisesRegex(
            expected_exception=AssertionError,
            expected_regex="Abstract method requires return type.",
        ):
            self._test_main_flow(
                target_folder="abstract_method_with_generics_without_return_type"
            )
