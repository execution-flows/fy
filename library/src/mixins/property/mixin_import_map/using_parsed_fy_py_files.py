from functools import cached_property

import abc

from mixins.property.parsed_fy_py_files.abc import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.required_property_setters_fy_py.abc import (
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
)
from mixins.property.project_root_folder.abc import (
    With_ProjectRootFolder_PropertyMixin_ABC,
)

from typing import Dict


class MixinImportMap_UsingParsedFyPyFiles_PropertyMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
    With_ProjectRootFolder_PropertyMixin_ABC,
    abc.ABC,
):
    @cached_property
    def _mixin_import_map(self) -> Dict[str, str]:
        return {}
