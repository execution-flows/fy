"""fy
property greeting: str using constant:
"""


# fy:start <<<===
class Greeting_UsingConstant_PropertyMixin:
    @property
    def _greeting(self) -> str:
        # fy:end <<<===
        return "Hello world!"