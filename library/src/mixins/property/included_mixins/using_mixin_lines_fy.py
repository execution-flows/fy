"""fy
from mixins.property.included_mixins.abc_fy import IncludedMixinsModel


property included_mixins: IncludedMixinsModel using mixin_lines:
    property fy_py_file_to_parse
    property mixin_lines
"""

import abc
import re
from functools import cached_property
from typing import List

from constants import FY_ENTITY_REGEX_STRING
from domain.fy_py_template_models import (
    PropertyMixinModel,
    AbstractPropertyModel,
    AbstractMethodModel,
    MethodMixinModel,
)
from domain.python_entity_name import PythonEntityName
from mixins.property.included_mixins.abc_fy import IncludedMixinsModel


from mixins.property.fy_py_file_to_parse.abc_fy import (
    FyPyFileToParse_PropertyMixin_ABC,
)
from mixins.property.mixin_lines.abc_fy import (
    MixinLines_PropertyMixin_ABC,
)


# fy:start ===>>>
class IncludedMixins_UsingMixinLines_PropertyMixin(
    # Property_mixins
    FyPyFileToParse_PropertyMixin_ABC,
    MixinLines_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _included_mixins(self) -> IncludedMixinsModel:
        # fy:end <<<===
        flow_method_regex = re.compile(
            rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )

        flow_property_regex = re.compile(
            rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )

        abstract_property_mixin_regex = re.compile(
            rf"^\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})$"
        )

        abstract_method_mixin_regex = re.compile(
            rf"^\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})$"
        )
        properties: List[PropertyMixinModel] = []
        abstract_properties: List[AbstractPropertyModel] = []
        abstract_methods: List[AbstractMethodModel] = []
        methods: List[MethodMixinModel] = []
        for mixin_line in self._mixin_lines:
            if mixin_line.strip() == "":
                continue

            flow_property_fy_search = flow_property_regex.search(mixin_line)

            if flow_property_fy_search is not None:
                properties.append(
                    PropertyMixinModel(
                        property_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("property_name")
                        ),
                        implementation_name=PythonEntityName.from_snake_case(
                            flow_property_fy_search.group("implementation_name")
                        ),
                    )
                )
                continue

            declared_abstract_property_mixin = abstract_property_mixin_regex.search(
                mixin_line
            )

            if declared_abstract_property_mixin is not None:
                abstract_properties.append(
                    AbstractPropertyModel(
                        property_name=PythonEntityName.from_snake_case(
                            declared_abstract_property_mixin.group(
                                "abstract_property_name"
                            )
                        )
                    )
                )
                continue

            declared_abstract_method_mixin = abstract_method_mixin_regex.search(
                mixin_line
            )

            if declared_abstract_method_mixin is not None:
                abstract_methods.append(
                    AbstractMethodModel(
                        method_name=PythonEntityName.from_snake_case(
                            declared_abstract_method_mixin.group("abstract_method_name")
                        )
                    )
                )
                continue

            flow_method_fy_search = flow_method_regex.search(mixin_line)

            if flow_method_fy_search is not None:
                methods.append(
                    MethodMixinModel(
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

        included_mixins = IncludedMixinsModel(
            abstract_method_mixins=abstract_methods,
            abstract_property_mixins=abstract_properties,
            method_mixins=methods,
            property_mixins=properties,
        )

        return included_mixins
