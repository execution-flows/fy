"""fy
method greet -> None using encrypt:
    with method encrypt
"""

import abc

from fy_py_files.test_fy_py_files.method_with_abstract_method.abc_fy import (
    With_Encrypt_MethodMixin_ABC,
)


# fy:start <<<===
class Greet_UsingEncrypt_MethodMixin(
    # Method_mixins
    With_Encrypt_MethodMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        # fy:end <<<===
        print(self._encrypt("Hello World!"))