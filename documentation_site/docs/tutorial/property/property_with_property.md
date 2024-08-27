# Property with another Property

In this code, the ___fy___ code is used to define a property with specific behaviors and integrations. The property `greeting` uses another property, `french_greeting`, to provide its value. This approach allows for modular and reusable property definitions. Here’s how each part of the code is defined and how it works:

## Syntax

```py title="mixins/property/greeting/using_french_greeting_fy.py" linenums="1"
"""fy
property greeting: str using french_greeting:
    with property french_greeting
"""

import abc

from mixins.property.french_greeting.abc_fy import (
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
```

## Breakdown of Syntax

1. `:::py property greeting: str using french_greeting:`
    - **Property Declaration:** Defines a property named `greeting` with a type of `:::py str` (string). 
    - **Implementation Name:** `using french_greeting` declares the name of the specific property implementation that is then referenced by the hosting flow when included in a flow.
2. `:::py with property french_greeting` 
    - **Property Integration:** Indicates that the `greeting` property depends on the `french_greeting` property. This means the value or behavior of `greeting` is derived from `french_greeting`. 
3. Code Generation:
    - **Automatic Code Generation:** The ___fy___ tool generates the code between `:::py # fy:start` and `:::py # fy:end`. This includes the class definition and the `:::py @property` method annotation and declaration. 
    - **Base classes:** `:::py With_FrenchGreeting_PropertyMixin_ABC` base class ensures the `:::py french_greeting` property is available. `:::py abc.ABC` is required because `:::py With_FrenchGreeting_PropertyMixin_ABC` is an abstract class.
4. User Input:
    - The only code the user needs to write is the `:::py property` definition within the `"""fy` block.
    - After boilerplate code generation, the user can add custom functionality, such as `:::py return self._french_greeting` to the property method body.
