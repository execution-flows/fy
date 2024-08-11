from typing import Self

from pydantic import BaseModel


class PythonEntityName(BaseModel):
    snake_case: str
    pascal_case: str

    @classmethod
    def from_snake_case(cls, snake_case_name: str) -> Self:
        snake_case_phrases = snake_case_name.split('__')
        pascal_case_phrases = [
            ''.join(snake_case_word.capitalize()
                    for snake_case_word in snake_case_phrase.split('_'))
            for snake_case_phrase in snake_case_phrases
        ]
        pascal_case_name = '_'.join(pascal_case_phrases)
        return cls(
            snake_case=snake_case_name,
            pascal_case=pascal_case_name,
        )
