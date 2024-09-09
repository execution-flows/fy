# Comparison with traditional programming ways

While this is more code than we would typically need in traditional programming, there is one key difference. To use `datetime.utcnow().isoformat()` as a `greeting` value, we need to define a property `greeting` that utilizes this value.

=== "fy"

    ```fy 
    property greeting: str using utc_now_iso_format:
    ```

=== "Python"

    ```py title="mixins/property/greeting/using_utc_now_iso_format_fy.py" linenums="1"
    """fy
    property greeting: str using utc_now_iso_format:
    """
    from datetime import datetime
    
    
    # fy:start ===>>>
    class Greeting_UsingUtcNowIsoFormat_PropertyMixin:
    
        @property
        def _greeting(self) -> str:
            # fy:end <<<===
            return datetime.utcnow().isoformat()
    ```

Then the flow would look like:

=== "fy"

    ```fy 
    flow Greet_UsingUtcNowIsoFormat -> None:
        property greeting using utc_now_iso_format
        method greet using greeting
    ```

=== "Python"

    ```python title="flows/greet__using_utc_now_iso_format__fy.py" linenums="1"
    """fy
    flow Greet_UsingUtcNowIsoFormat -> None:
        property greeting using utc_now_iso_format
        method greet using greeting
    """
    from fy_core.base.flow_base import FlowBase
    
    from mixins.method.greet.using_greeting_fy import (
        Greet_UsinGreeting_MethodMixin,
    )
    from mixins.property.greeting.using_utc_now_iso_format_fy import (
        Greeting_UsingUtcNowIsoFormat_PropertyMixin,
    )
    
    
    # fy:start ===>>>
    class Greet_UsingUtcNowIsoFormat_Flow(
        # Property Mixins
        Greeting_UsingUtcNowIsoFormat_PropertyMixin,
        # Method Mixins
        Greet_UsinGreeting_MethodMixin,
        # Base
        FlowBase[None],
    ):
        def __call__(self) -> None:
            # fy:end <<<===
            self._greet()
    ```

We can explicitly see that usage of `datetime.utcnow().isoformat()` is not an accident or error, but is intentional. 
