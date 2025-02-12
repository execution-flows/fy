# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy

from typing import List
from fy_library.domain.parsed_fy_py_file import ParsedFyPyFile


property parsed_fy_py_files_with_own_abstract_mixin: List[ParsedFyPyFile] using parsed_fy_py_files_map_by_key:
    property parsed_fy_py_files_map_by_key
fy"""

import abc
from functools import cached_property
from typing import List, cast

from fy_library.domain.mixin_models import (
    AbstractPropertyModel,
    MixinModelKind,
    AbstractMethodModel,
)
from fy_library.domain.parsed_fy_py_file import (
    ParsedFyPyFile,
    ParsedMethodFyPyFile,
    ParsedAbstractMethodFyPyFile,
    ParsedAbstractPropertyFyPyFile,
    ParsedPropertyFyPyFile,
)
from fy_library.domain.parsed_fy_py_file_kind import ParsedFyPyFileKind
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py.parsed_fy_py_files_with_own_abstract_mixin.abc_fy import (
    ParsedFyPyFilesWithOwnAbstractMixin_PropertyMixin_ABC,
)


# fy:start ===>>>
class ParsedFyPyFilesWithOwnAbstractMixin_UsingParsedFyPyFilesMapByKey_PropertyMixin(
    # Property Mixins
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
                    own_abstract_method_entity_key = (
                        ParsedFyPyFileKind.ABSTRACT_METHOD,
                        parsed_method_fy_py_file.method_name.snake_case,
                    )
                    if (
                        own_abstract_method_entity_key
                    ) not in self._parsed_fy_py_files_map_by_key:
                        return parsed_fy_py_file

                    parsed_abstract_method_fy_py_file = cast(
                        ParsedAbstractMethodFyPyFile,
                        self._parsed_fy_py_files_map_by_key[
                            own_abstract_method_entity_key
                        ],
                    )

                    if any(
                        abstract_method_mixin.python_class_name.pascal_case
                        == parsed_abstract_method_fy_py_file.python_class_name.pascal_case
                        for abstract_method_mixin in parsed_method_fy_py_file.abstract_method_mixins
                    ):
                        return parsed_fy_py_file

                    return ParsedMethodFyPyFile.model_validate(
                        {
                            **parsed_method_fy_py_file.model_dump(),
                            "abstract_method_mixins": parsed_method_fy_py_file.abstract_method_mixins
                            + [
                                AbstractMethodModel(
                                    python_class_name=parsed_abstract_method_fy_py_file.python_class_name,
                                    kind=MixinModelKind.ABSTRACT_METHOD,
                                    method_name=parsed_abstract_method_fy_py_file.abstract_method_name,
                                    generics_impl=(
                                        parsed_method_fy_py_file.generics_def
                                        if parsed_abstract_method_fy_py_file.generics_def
                                        != ""
                                        else ""
                                    ),
                                    return_type="",
                                )
                            ],
                        }
                    )
                case ParsedFyPyFileKind.PROPERTY:
                    parsed_property_fy_py_file = cast(
                        ParsedPropertyFyPyFile, parsed_fy_py_file
                    )
                    own_abstract_property_entity_key = (
                        ParsedFyPyFileKind.ABSTRACT_PROPERTY,
                        parsed_property_fy_py_file.property_name.snake_case,
                    )
                    if (
                        own_abstract_property_entity_key
                    ) not in self._parsed_fy_py_files_map_by_key:
                        return parsed_fy_py_file

                    parsed_abstract_property_fy_py_file = cast(
                        ParsedAbstractPropertyFyPyFile,
                        self._parsed_fy_py_files_map_by_key[
                            own_abstract_property_entity_key
                        ],
                    )

                    if any(
                        abstract_mixin.python_class_name.pascal_case
                        == parsed_abstract_property_fy_py_file.python_class_name.pascal_case
                        for abstract_mixin in parsed_property_fy_py_file.abstract_property_mixins
                    ):
                        return parsed_fy_py_file

                    return ParsedPropertyFyPyFile.model_validate(
                        {
                            **parsed_property_fy_py_file.model_dump(),
                            "abstract_property_mixins": parsed_property_fy_py_file.abstract_property_mixins
                            + [
                                AbstractPropertyModel(
                                    python_class_name=parsed_abstract_property_fy_py_file.python_class_name,
                                    kind=MixinModelKind.ABSTRACT_PROPERTY,
                                    property_name=parsed_property_fy_py_file.property_name,
                                    generics_impl=(
                                        parsed_property_fy_py_file.generics_def
                                        or parsed_property_fy_py_file.property_type
                                    )
                                    if parsed_abstract_property_fy_py_file.generics_def
                                    != ""
                                    else "",
                                    property_type="",
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
