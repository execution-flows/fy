# Property in Property

In this code, the `fy` tool is used to define a property with specific behaviors and integrations. The property `greeting` uses another property, `french_greeting`, to provide its value. This approach allows for modular and reusable property definitions across different classes. Here’s how each part of the code is defined and how it works:

## Syntax
```py linenums="1"
"""fy
property greeting: str using french_greeting:
    with property french_greeting
"""

import abc

from fy_py_files.test_fy_py_files.property_with_property.abc_fy import (
    With_FrenchGreeting_PropertyMixin_ABC,
)


# fy:start <<<===
class Greeting_UsingFrenchGreeting_PropertyMixin(
    # Property Mixins
    With_FrenchGreeting_PropertyMixin_ABC,
    abc.ABC,
):
    @property
    def _greeting(self) -> str:
        # fy:end <<<===
        return self._french_greeting

    @_greeting.setter
    def _greeting(self, greeting: str) -> None:
        self.__greeting = greeting
```

## Breakdown of Syntax
1. `:::py property greeting: str using french_greeting:`
    - **Property Declaration:** Defines a property named `greeting` with a type of `:::py str` (string). 
    - **Using Another Property:** using `french_greeting` specifies that the `greeting` property will use the value from another property named `french_greeting`.
2. `:::py with property french_greeting` 
    - **Property Integration:** Indicates that the `greeting` property depends on the `french_greeting` property. This means the value or behavior of `greeting` is derived from `french_greeting`. 
3. Code Generation:
    - **Automatic Code Generation:** The `fy` tool generates the code between `:::py # fy:start` and `:::py # fy:end`. This includes the class definition and the property implementations. 
    - **Imports:** Imports `:::py With_FrenchGreeting_PropertyMixin_ABC` to ensure the `:::py french_greeting` property is available, and `:::py abc.ABC` to support abstract base class functionality.
