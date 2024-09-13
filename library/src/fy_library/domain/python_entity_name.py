# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from typing import Final

from pydantic import BaseModel

_PASCAL_CASE_REGEX: Final = re.compile("(?<=.)(?=[A-Z])")


class PythonEntityName(BaseModel):
    snake_case: str
    pascal_case: str

    @classmethod
    def from_snake_case(cls, snake_case_name: str) -> "PythonEntityName":
        snake_case_phrases = snake_case_name.split("__")
        pascal_case_phrases = [
            "".join(
                snake_case_word.capitalize()
                for snake_case_word in snake_case_phrase.split("_")
            )
            for snake_case_phrase in snake_case_phrases
        ]
        pascal_case_name = "_".join(pascal_case_phrases)
        return cls(
            snake_case=snake_case_name,
            pascal_case=pascal_case_name,
        )

    @classmethod
    def from_pascal_case(cls, pascal_case_name: str) -> "PythonEntityName":
        pascal_case_phrases = pascal_case_name.split("_")
        snake_case_phrases = [
            "_".join(
                pascal_case_word.lower()
                for pascal_case_word in _PASCAL_CASE_REGEX.split(pascal_case_phrase)
            )
            for pascal_case_phrase in pascal_case_phrases
        ]
        snake_case_name = "__".join(snake_case_phrases)
        return cls(
            snake_case=snake_case_name,
            pascal_case=pascal_case_name,
        )
