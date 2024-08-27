# Property in Flow

In the _fy_ syntax, a _property_ is a class mixin that defines a `:::py @property` that provides data to the hosting flow. Properties can be defined in different ways, depending on how the data is intended to be used or modified. For instance, a property can fetch the data from a database or a third party API. Or it can compute it using other properties in included in the flow.

In the _fy_ syntax, a _property_ is a class mixin that defines a method annotated with `:::py @property` Python annotation to provide data to the hosting flow. Properties can be defined in various ways, depending on how the data is intended to be used or modified. For instance, a property might fetch data from a database or a third-party API, or it could compute data using other properties included in the flow.

## Syntax

```py title="mixins/property/greeting/using_hello_world_fy.py" linenums="1" 
"""fy
flow HelloWorld_UsingGreeting -> None:
    property greeting using hello_world
"""

from base.flow_base import FlowBase

from mixins.property.greeting.using_hello_world_fy import (
    Greeting_UsingHelloWorld_PropertyMixin,
)


# fy:start <<<===
class HelloWorld_UsingGreeting_Flow(
    # Property Mixins
    Greeting_UsingHelloWorld_PropertyMixin,
    # Base
    FlowBase[None]
):
    def __call__(self) -> None:
        # fy:end <<<===
        print(self._greeting)
```

## Breakdown of Syntax

1. `:::py flow HelloWorld_UsingGreeting -> None:`
    - Declares a new flow named `:::py HelloWorld_UsingGreeting`, which is implemented as a Python class that uses property as a mixin.
    - `:::py -> None` specifies the return type of the flow, which in this case is `:::py None`.
2. `:::py property greeting using hello_world`
    - Declares a property named `:::py greeting` with a constant value or predefined behavior.
3. Code Generation:
    - **Automatic Code Generation:** The `fy` tool generates code between `:::py # fy:start` and `:::py # fy:end` including the class definition and the method declaration. 
    - The generated code includes the class definition `:::py HelloWorld_UsingGreeting_Flow`, which incorporates the `:::py Greeting_UsingHelloWorld_PropertyMixin` mixin and the `:::py FlowBase` base class. 
    - **Imports:** Includes necessary imports, such as `:::py Greeting_UsingHelloWorld_PropertyMixin`, which contains the `:::py greeting` property.
    - The `:::py __call__` method prints the value of the _greeting property.
4. User Input:
    - The only code the user needs to write is the `:::py flow` declaration within the `"""fy` block. After generation, the user can add custom functionality, such as `:::py print(self._greeting)`.

## Summary

In `fy`, defining a property in a flow allows you to encapsulate data as an attribute that can be used within the flow's included property and method mixins. A flow can include property implementation that fits its needs, like fetching data from the database or providing a constant value. This makes it easy to manage state and logic in a modular and intuitive way.
