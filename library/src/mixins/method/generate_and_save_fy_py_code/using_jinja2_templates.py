import abc

from mixins.property.parsed_fy_py_files.abc import (
    With_ParsedFyPyFiles_PropertyMixin_ABC,
)
from mixins.property.required_property_setters_fy_py.abc import (
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
)
from mixins.property.mixin_import_map.abc import With_MixinImportMap_PropertyMixin_ABC


class GenerateAndSaveFyPyFiles_UsingJinja2Templates_MethodMixin(
    # Property_mixins
    With_ParsedFyPyFiles_PropertyMixin_ABC,
    With_RequiredPropertySettersFyPy_PropertyMixin_ABC,
    With_MixinImportMap_PropertyMixin_ABC,
    abc.ABC,
):
    def _generate_and_save_fy_py_files(self) -> None:
        print(self._parsed_fy_py_files)
        print(self._required_property_setters_fy_py)
        print(self._mixin_import_map)
