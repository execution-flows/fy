# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from unittest import TestCase

from domain.python_entity_name import PythonEntityName


class TestPythonEntityName(TestCase):
    def test_from_snake_case(self) -> None:
        snake_case = "phrase_one__phrase_two"
        pascal_case_expected = "PhraseOne_PhraseTwo"
        snake_case_expected = snake_case
        generated_actual_cases = PythonEntityName.from_snake_case(snake_case)

        self.assertEqual(
            first=snake_case_expected, second=generated_actual_cases.snake_case
        )
        self.assertEqual(
            first=pascal_case_expected, second=generated_actual_cases.pascal_case
        )

    def test_from_pascal_case(self) -> None:
        pascal_case = "PhraseOne_PhraseTwo"
        pascal_case_expected = pascal_case
        snake_case_expected = "phrase_one__phrase_two"
        generated_actual_cases = PythonEntityName.from_pascal_case(pascal_case)

        self.assertEqual(
            first=snake_case_expected, second=generated_actual_cases.snake_case
        )
        self.assertEqual(
            first=pascal_case_expected, second=generated_actual_cases.pascal_case
        )
