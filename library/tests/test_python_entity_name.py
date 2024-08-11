from unittest import TestCase

from domain.python_entity_name import PythonEntityName


class TestPythonEntityName(TestCase):
    def test_from_snake_case(self) -> None:
        snake_case = "phrase_one__phrase_two"
        pascal_case_expected = "PhraseOne_PhraseTwo"
        snake_case_expected = snake_case
        generated_actual_cases = PythonEntityName.from_snake_case(snake_case)

        self.assertEqual(snake_case_expected, generated_actual_cases.snake_case)
        self.assertEqual(pascal_case_expected, generated_actual_cases.pascal_case)

    def test_from_pascal_case(self) -> None:
        pascal_case = "PhraseOne_PhraseTwo"
        pascal_case_expected = pascal_case
        snake_case_expected = "phrase_one__phrase_two"
        generated_actual_cases = PythonEntityName.from_pascal_case(pascal_case)

        self.assertEqual(snake_case_expected, generated_actual_cases.snake_case)
        self.assertEqual(pascal_case_expected, generated_actual_cases.pascal_case)
