# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.fy_py_template_models import BaseMixinModel


property mixin_models: List[BaseMixinModel] using mixin_lines:
    property fy_py_file_to_parse
    property mixin_lines
"""

import re
from functools import cached_property
from fy_library.domain.fy_py_template_models import (
    BaseMixinModel,
    PropertyMixinModel,
    MixinModelKind,
    AbstractPropertyModel,
    AbstractMethodModel,
    MethodMixinModel,
)
from typing import List
from fy_library.constants import FY_ENTITY_REGEX_STRING
from fy_library.domain.python_entity_name import PythonEntityName
from fy_library.mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from fy_library.mixins.property.mixin_lines.abc_fy import (
    MixinLines_PropertyMixin_ABC,
)
import abc

_FLOW_METHOD_REGEX = re.compile(
    rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)

_FLOW_PROPERTY_REGEX = re.compile(
    rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
    rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
)

_ABSTRACT_PROPERTY_MIXIN_REGEX = re.compile(
    rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})$"
)

_ABSTRACT_METHOD_MIXIN_REGEX = re.compile(
    rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})$"
)


# fy:start ===>>>
class MixinModels_UsingMixinLines_PropertyMixin(
    # Property_mixins
    FyPyFileToParse_PropertyMixin_ABC,
    MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_models(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        mixin_models: List[BaseMixinModel] = []

        for mixin_line in self._mixin_lines:
            if mixin_line.strip() == "":
                continue

            # Flow mixin_line to mixin_model

            flow_property_fy_search = _FLOW_PROPERTY_REGEX.search(mixin_line)

            if flow_property_fy_search is not None:
                mixin_models.append(
                    PropertyMixinModel(
                        kind=MixinModelKind.PROPERTY,
                        property_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("property_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("implementation_name")
                        ),
                    )
                )
                continue

            declared_abstract_property_mixin = _ABSTRACT_PROPERTY_MIXIN_REGEX.search(
                mixin_line
            )

            if declared_abstract_property_mixin is not None:
                mixin_models.append(
                    AbstractPropertyModel(
                        kind=MixinModelKind.ABSTRACT_PROPERTY,
                        property_name=PythonEntityName.from_snake_case(
                            declared_abstract_property_mixin.group(
                                "abstract_property_name"
                            )
                        ),
                    )
                )
                continue

            declared_abstract_method_mixin = _ABSTRACT_METHOD_MIXIN_REGEX.search(
                mixin_line
            )

            if declared_abstract_method_mixin is not None:
                mixin_models.append(
                    AbstractMethodModel(
                        kind=MixinModelKind.ABSTRACT_METHOD,
                        method_name=PythonEntityName.from_snake_case(
                            declared_abstract_method_mixin.group("abstract_method_name")
                        ),
                    )
                )
                continue

            flow_method_fy_search = _FLOW_METHOD_REGEX.search(mixin_line)

            if flow_method_fy_search is not None:
                mixin_models.append(
                    MethodMixinModel(
                        kind=MixinModelKind.METHOD,
                        method_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("method_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_method_fy_search.group("implementation_name")
                        ),
                    )
                )
                continue

            raise ValueError(
                f"Line {mixin_line} in {self._fy_py_file_to_parse} is invalid."
            )

        return mixin_models
