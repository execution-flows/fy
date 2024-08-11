from unittest import TestCase

from domain.python_entity_name import PythonEntityName


class TestPythonEntityName(TestCase):
    def test_python_entity_name(self) -> None:
        snake_case_expected = "phrase_one__phrase_two"
        pascal_case_expected = "PhraseOne_PhraseTwo"

        generated_actual_cases = PythonEntityName.from_snake_case(snake_case_expected)

        self.assertEqual(snake_case_expected, generated_actual_cases.snake_case)
        self.assertEqual(pascal_case_expected, generated_actual_cases.pascal_case)
