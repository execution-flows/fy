# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pathlib import Path

from flow_compose_tests.test_utils.main_flow_compose_test_case import (
    MainFlowComposeTestCase,
)


class TestGenerateSubdirectoryOnly(MainFlowComposeTestCase):
    def test_generate_subdirectory_only(self) -> None:
        self._test_main_flow(
            target_folder="generate_subdirectory_only",
            folder_to_generate="subdirectory",
        )

        folder_to_parse = (
            Path(__file__).parent.parent
            / "test_flow_compose_files"
            / "generate_subdirectory_only"
        )

        self.assertFalse((folder_to_parse / "flow_fc.py").exists())
