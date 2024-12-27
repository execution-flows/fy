# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy

from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files_with_own_abstract_mixin: List[ParsedFyPyFile] using parsed_fy_py_files_map_by_key:
    property parsed_fy_py_files_map_by_key
"""

from functools import cached_property
import abc

from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from typing import List, cast
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedFyPyFileKind,
    ParsedMethodFyPyFile,
    convert_parsed_abstract_method_fy_py_file_to_abstract_method_mixin,
    ParsedAbstractMethodFyPyFile,
    ParsedAbstractPropertyFyPyFile,
    convert_parsed_abstract_property_fy_py_file_to_abstract_method_mixin,
    ParsedPropertyFyPyFile,
)

from fy_library.mixins.property.parsed_fy_py_files_with_own_abstract_mixin.abc_fy import (
    ParsedFyPyFilesWithOwnAbstractMixin_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFilesWithOwnAbstractMixin_UsingParsedFyPyFilesMapByKey_PropertyMixin(
    # Property_mixins
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    ParsedFyPyFilesWithOwnAbstractMixin_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _parsed_fy_py_files_with_own_abstract_mixin(self) -> List[ParsedFyPyFile]:
        # fy:end <<<===
        def with_own_abstract_mixin_if_exists(
            parsed_fy_py_file: ParsedFyPyFile,
        ) -> ParsedFyPyFile:
            match parsed_fy_py_file.file_type:
                case (
                    ParsedFyPyFileKind.FLOW
                    | ParsedFyPyFileKind.BASE_FLOW
                    | ParsedFyPyFileKind.ABSTRACT_PROPERTY
                    | ParsedFyPyFileKind.ABSTRACT_METHOD
                    | ParsedFyPyFileKind.PROPERTY_SETTER
                ):
                    return parsed_fy_py_file
                case ParsedFyPyFileKind.METHOD:
                    parsed_method_fy_py_file = cast(
                        ParsedMethodFyPyFile, parsed_fy_py_file
                    )
                    if (
                        parsed_method_fy_py_file.method_name.snake_case
                        not in self._parsed_fy_py_files_map_by_key
                    ):
                        return parsed_fy_py_file

                    parsed_abstract_method_fy_py_file = cast(
                        ParsedAbstractMethodFyPyFile,
                        self._parsed_fy_py_files_map_by_key[
                            parsed_method_fy_py_file.method_name.snake_case
                        ],
                    )

                    return ParsedMethodFyPyFile.model_validate(
                        {
                            **parsed_method_fy_py_file.model_dump(),
                            "abstract_method_mixins": parsed_method_fy_py_file.abstract_method_mixins
                            + [
                                convert_parsed_abstract_method_fy_py_file_to_abstract_method_mixin(
                                    parsed_abstract_method_fy_py_file=parsed_abstract_method_fy_py_file
                                )
                            ],
                        }
                    )
                case ParsedFyPyFileKind.PROPERTY:
                    parsed_property_fy_py_file = cast(
                        ParsedPropertyFyPyFile, parsed_fy_py_file
                    )
                    if (
                        parsed_property_fy_py_file.property_name.snake_case
                        not in self._parsed_fy_py_files_map_by_key
                    ):
                        return parsed_fy_py_file

                    parsed_abstract_property_fy_py_file = cast(
                        ParsedAbstractPropertyFyPyFile,
                        self._parsed_fy_py_files_map_by_key[
                            parsed_property_fy_py_file.property_name.snake_case
                        ],
                    )

                    return ParsedPropertyFyPyFile.model_validate(
                        {
                            **parsed_property_fy_py_file.model_dump(),
                            "abstract_property_mixins": parsed_property_fy_py_file.abstract_property_mixins
                            + [
                                convert_parsed_abstract_property_fy_py_file_to_abstract_method_mixin(
                                    parsed_abstract_property_fy_py_file=parsed_abstract_property_fy_py_file
                                )
                            ],
                        }
                    )

        return [
            with_own_abstract_mixin_if_exists(
                parsed_fy_py_file=self._parsed_fy_py_files_map_by_key[
                    parsed_fy_py_file_key
                ]
            )
            for parsed_fy_py_file_key in self._parsed_fy_py_files_map_by_key
        ]
