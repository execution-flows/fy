# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from fy_library.domain.fy_py_template_models import BaseTemplateModel


property template_model: BaseTemplateModel using parsed_fy_py_file:
    property parsed_fy_py_file
    property parsed_fy_py_files_map_by_key
    property abstract_entities_ordering_index
"""

import abc
from functools import cached_property

from fy_library.domain.fy_py_template_models import (
    BaseTemplateModel,
)
from fy_library.flows.create_template_model_using_parsed_fy_py_file.main_fy import (
    CreateTemplateModelUsingParsedFyPyFile_Flow,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)
from fy_library.mixins.property.parsed_fy_py_files_map_by_key.abc_fy import (
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
)

from fy_library.mixins.property.ordered_abstract_entities.abc_fy import (
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
)

from fy_library.mixins.property.template_model.abc_fy import (
    TemplateModel_PropertyMixin_ABC,
)


# fy:start ===>>>
class TemplateModel_UsingParsedFyPyFile_PropertyMixin(
    # Property_mixins
    AbstractEntitiesOrderingIndex_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    ParsedFyPyFilesMapByKey_PropertyMixin_ABC,
    TemplateModel_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _template_model(self) -> BaseTemplateModel:
        # fy:end <<<===
        return CreateTemplateModelUsingParsedFyPyFile_Flow(
            parsed_fy_py_file=self._parsed_fy_py_file,
            parsed_fy_py_files_map_by_key=self._parsed_fy_py_files_map_by_key,
            abstract_entities_ordering_index=self._abstract_entities_ordering_index,
        )()
