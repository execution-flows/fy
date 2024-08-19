from functools import cached_property


class Greeting_UsingConstant_PropertyMixin:
    @cached_property
    def _greeting(self) -> str:
        return "Hello world!"
