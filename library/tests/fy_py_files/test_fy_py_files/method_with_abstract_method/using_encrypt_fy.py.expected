"""fy
method greet -> None using encrypt:
    method encrypt
"""

import abc
from fy_py_files.test_fy_py_files.method_with_abstract_method.abc_fy import (
    Encrypt_MethodMixin_ABC,
)


# fy:start ===>>>
class Greet_UsingEncrypt_MethodMixin(
    # Method_mixins
    Encrypt_MethodMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        # fy:end <<<===
        print(self._encrypt("Hello World!"))
