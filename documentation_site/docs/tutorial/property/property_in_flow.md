# Property Included in a Flow

In the ___fy___ syntax, a _property_ is a class mixin that defines a method annotated with `:::py @property` Python annotation to provide data to the encapsulating flow. Properties can be defined in various ways, depending on how the data is intended to be used or modified. For instance, a property might fetch data from a database or a third-party API, or it could compute data using other properties included in the flow.

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
    FlowBase[None],
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
    - The ___fy___ tool generates code between `:::py # fy:start` and `:::py # fy:end` including the class definition and the method declaration. 
    - The generated code includes the class definition `:::py HelloWorld_UsingGreeting_Flow`, which incorporates the `:::py Greeting_UsingHelloWorld_PropertyMixin` mixin and the `:::py FlowBase` base class. 
    - The `Greeting_UsingHelloWorld_PropertyMixin` import statement is automatically added once in the file. When the ___fy___ tool detects this import in the code, it skips adding it again to avoid disrupting the import order.
    - The declaration of `:::py __call__(self) -> None:` method.
4. User Input:
    - The only code the user needs to write is the `:::py flow` declaration within the `"""fy` block.
    - After boilerplate code generation, the user can add custom functionality, such as `:::py print(self._greeting)`.

## Summary

In ___fy___, defining a property in a flow allows you to encapsulate data as an attribute that is used by other property and method mixins included in a flow. A flow can include property implementation that fits its needs, like fetching data from the database or providing a constant value. This makes it easy to manage state and logic in a modular and intuitive way.
