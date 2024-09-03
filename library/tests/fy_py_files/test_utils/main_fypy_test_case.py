# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
import re
from pathlib import Path
from unittest import TestCase

from fy_library.constants import (
    FY_PY_FILE_EXTENSION,
    FY_START_MARKER,
    FY_END_MARKER,
    FY_PY_FILE_SIGNATURE,
    FY_CODE_FILE_END_SIGNATURE,
)
from fy_library.flows.fy_py_main_fy import FyPy_Main_Flow

_GENERATED_CONTENT_REGEX = re.compile(
    rf"^(?P<fy_code>.*{FY_PY_FILE_SIGNATURE}.*{FY_CODE_FILE_END_SIGNATURE}\n)"
    r"(?P<imports>.*)"
    rf"{FY_START_MARKER}(?P<generated_code>.*){FY_END_MARKER}\n"
    r"(?P<post_generated_code>.*)$",
    flags=re.DOTALL,
)


class MainFyPyTestCase(TestCase):

    def _test_main_flow(
        self,
        target_folder: str,
        perform_fy_code_deletion: bool = True,
        perform_imports_deletion: bool = True,
    ) -> None:
        folder_to_parse = (
            Path(__file__).parent.parent / "test_fy_py_files" / target_folder
        )

        test_cases = (
            [(True, True), (True, False), (False, True), (False, False)]
            if perform_fy_code_deletion and perform_imports_deletion
            else [(perform_fy_code_deletion, perform_imports_deletion)]
        )
        for (
            test_case_perform_fy_code_deletion,
            test_case_imports_deletion,
        ) in test_cases:
            if test_case_perform_fy_code_deletion or test_case_imports_deletion:
                self.__remove_fy_generated_code_and_imports_from_generated_files(
                    folder_to_parse,
                    perform_fy_code_deletion=test_case_perform_fy_code_deletion,
                    perform_imports_deletion=test_case_imports_deletion,
                )

            FyPy_Main_Flow(
                folder_to_parse=folder_to_parse,
                project_root_folder=Path(__file__).parent.parent.parent,
            )()

            self.__test_fy_py_files_in_directory(folder_to_parse)

    def __assert_files_equal(
        self, file_to_expect: Path, file_to_generate: Path, comparing_file_path: Path
    ) -> None:
        with (
            file_to_expect.open() as expected_py_file,
            file_to_generate.open() as generated_py_file,
        ):
            self.assertEqual(
                expected_py_file.read(),
                generated_py_file.read(),
                f"Comparing {comparing_file_path}",
            )

    def __remove_fy_generated_code_and_imports_from_generated_files(
        self,
        folder_to_parse: Path,
        perform_fy_code_deletion: bool,
        perform_imports_deletion: bool,
    ) -> None:
        fy_files_in_directory = list(folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            with open(file=fy_file_path, mode="r") as f:
                file_content = f.read()

            generated_content_search = _GENERATED_CONTENT_REGEX.search(file_content)

            if generated_content_search is None:
                continue

            cleaned_file_content = (
                f"{generated_content_search.group('fy_code')}"
                f"{generated_content_search.group('imports') if not perform_imports_deletion else ''}"
                f"{FY_START_MARKER}\n"
                f"{generated_content_search.group('generated_code') if not perform_fy_code_deletion else ''}"
                f"{FY_END_MARKER}\n"
                f"{generated_content_search.group('post_generated_code')}"
            )
            with open(file=fy_file_path, mode="w") as f:
                f.write(cleaned_file_content)

    def __test_fy_py_files_in_directory(self, folder_to_parse: Path) -> None:
        fy_files_in_directory = list(folder_to_parse.rglob(f"*{FY_PY_FILE_EXTENSION}"))

        assert len(fy_files_in_directory) > 0, f"Folder {folder_to_parse} is empty"

        for fy_file_path in fy_files_in_directory:
            if not fy_file_path.is_file():
                continue

            self.__assert_files_equal(
                file_to_expect=fy_file_path.with_name(f"{fy_file_path.name}.expected"),
                file_to_generate=fy_file_path,
                comparing_file_path=fy_file_path,
            )
