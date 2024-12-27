# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from .test_utils.main_fypy_test_case import MainFyPyTestCase


class TestSortingAbstractsInBaseFlow(MainFyPyTestCase):
    def test_sorting_abstracts_in_base_flow(self) -> None:
        self._test_main_flow(target_folder="base_flow_ordering_abstract_mixins")

        from .test_fy_py_files.ordered_abstract_methods_test.flow_fy import (
            Message_Flow,
        )

        self.assertEqual(
            Message_Flow()(),
            "required_1required_2required_2required_1required_1required_2",
        )
