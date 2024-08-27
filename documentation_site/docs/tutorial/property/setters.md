# Property Setters

When using the _Execution Flows_ ___fy___ tool, writing a property setter manually involves defining a property and then adding a `@<property_name>.setter` method to manage how the property value is assigned. Alternatively, the ___fy___ tool simplifies this process by generating the necessary boilerplate code. You can declare an abstract property and include `property <property_name> using setter` in the flow mixins, allowing the tool to automatically handle the setter implementation. This approach streamlines property management in your code.


## Automatically Generated Setter Implementation

When a flow declares a setter, the ___fy___ tool checks if a setter implementation for the defined property exists. If it does not find the implementation, it generates one. 

Below is an example of the generated code for a setter for the `property greeting: str`.

### Example

Abstract property definition:

```py title="mixins/property/greeting/abc_fy.py" linenums="1"
"""fy
property greeting: str
"""

import abc


# fy:start <<<===
class With_Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()

```

Property setter defined as a flow mixin:

```py title="flows/hello_world_using_setter_fy.py" linenums="1" 
"""fy
flow HelloWorld_UsingGreeting -> None:
    property greeting using setter
"""
from typing import Any

from base.flow_base import FlowBase

from mixins.property.greeting.using_setter_fy import (
    Greeting_UsingSetter_PropertyMixin,
)


# fy:start <<<===
class HelloWorld_UsingSetter_Flow(
    # Property Mixins
    Greeting_UsingSetter_PropertyMixin,
    # Base
    FlowBase[None]
):
    def __call__(self) -> None:
        # fy:end <<<===
        print(self._greeting)

    def __init__(
        self,
        *args: Any,
        greeting: str,
        **kwargs: Any,
    ) -> None:
        self._greeting = greeting
        super().__init__(*args, **kwargs)
```

A Python file generated by the ___fy___ tool

```py title="mixins/property/greeting/using_setter.py" linenums="1"
# fy:start <<<===
class Greeting_UsingSetter_PropertyMixin:
    @property
    def _greeting(self) -> str:
        raise NotImplementedError()

    @_greeting.setter
    def _greeting(self, value: str) -> None:
        raise NotImplementedError()
        # fy:end <<<===
```