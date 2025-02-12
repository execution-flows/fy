"""fy
method greet(greeting_text: str) -> int using constant:
    property greeting
fy"""


# fy:start ===>>>
class Greet_UsingEncrypt_MethodMixin:
    def _greet(self, greeting_text: str) -> int:
        # fy:end <<<===
        print(greeting_text)
        return 1
