# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
"""fy
from typing import List
from fy_library.domain.mixin_models import BaseMixinModel


property abstract_mixins: List[BaseMixinModel] using parsed_method_fy_py_file:
    property parsed_fy_py_file
"""

import abc
from functools import cached_property
from typing import List, cast

from fy_library.domain.mixin_models import BaseMixinModel
from fy_library.domain.parsed_fy_py_file import (
    ParsedMethodFyPyFile,
)
from fy_library.mixins.property.parsed_fy_py_file.abc_fy import (
    ParsedFyPyFile_PropertyMixin_ABC,
)

from fy_library.mixins.property.abstract_mixins.abc_fy import (
    AbstractMixins_PropertyMixin_ABC,
)


# fy:start ===>>>
class AbstractMixins_UsingParsedMethodFyPyFile_PropertyMixin(
    # Property_mixins
    AbstractMixins_PropertyMixin_ABC,
    ParsedFyPyFile_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _abstract_mixins(self) -> List[BaseMixinModel]:
        # fy:end <<<===
        parsed_method_fy_py_file = self._parsed_fy_py_file
        assert isinstance(parsed_method_fy_py_file, ParsedMethodFyPyFile)

        return cast(
            List[BaseMixinModel],
            parsed_method_fy_py_file.abstract_property_mixins
            + parsed_method_fy_py_file.abstract_method_mixins,
        )
