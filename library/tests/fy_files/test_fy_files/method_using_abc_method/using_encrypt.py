import abc

from fy_files.test_fy_files.method_using_abc_method.abc import Encrypt_MethodMixin_ABC


class Greet_UsingEncrypt_MethodMixin(
    # Method_mixins
    Encrypt_MethodMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        print(self._encrypt("Hello World!"))