# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pathlib import Path
from unittest import TestCase

from fy_library.flows.flow_compose_main_fy import FlowCompose_Main_Flow


class MainFlowComposeTestCase(TestCase):
    def _test_main_flow(
        self,
        target_folder: str,
    ) -> None:
        folder_to_parse = (
            Path(__file__).parent.parent / "test_flow_compose_files" / target_folder
        )

        self.__remove_flow_compose_generated_code(
            folder_to_parse,
        )

        FlowCompose_Main_Flow(
            folder_to_parse=folder_to_parse,
            project_root_folder=Path(__file__).parent.parent.parent,
        )()

        self.__test_flow_compose_files_in_directory(folder_to_parse)

    def __remove_flow_compose_generated_code(
        self,
        folder_to_parse: Path,
    ) -> None:
        fc_files_in_directory = list(folder_to_parse.rglob("_fc.py"))

        if len(fc_files_in_directory) == 0:
            return

        for fc_file_path in fc_files_in_directory:
            if not fc_file_path.is_file():
                continue

            fc_file_path.unlink()

    def __test_flow_compose_files_in_directory(self, folder_to_parse: Path) -> None:
        fc_files_in_directory = list(folder_to_parse.rglob("*_fc.py"))

        assert len(fc_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fc_file_path in fc_files_in_directory:
            if not fc_file_path.is_file():
                continue

            self.__assert_files_equal(
                file_to_expect=fc_file_path.with_name(f"{fc_file_path.name}.expected"),
                file_to_generate=fc_file_path,
            )

    def __assert_files_equal(
        self, file_to_expect: Path, file_to_generate: Path
    ) -> None:
        with (
            file_to_expect.open() as expected_py_file,
            file_to_generate.open() as generated_py_file,
        ):
            self.assertEqual(
                expected_py_file.read(),
                generated_py_file.read(),
                f"Comparing {generated_py_file}",
            )
