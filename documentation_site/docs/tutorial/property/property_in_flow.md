# Property in Flow

In the _fy_ syntax, a _property_ is a variable or attribute associated with a flow (similar to a class attributes in Python) that stores data. Properties can be defined in different ways, depending on how the data is intended to be used or modified. For instance, a property can be defined using a constant, which means the value assigned to this property remains fixed throughout the flow's lifecycle.

## Syntax

```fy title="Flow using Property" linenums="1" 
flow HelloWorld:
    property greeting using constant

    def -> None:
        print(self._greeting)

```
## Breakdown of Syntax
1. `:::py flow HelloWorld:`
    - creates a new flow named `HelloWorld`.
2. `:::py property greeting using constant`
    - Defines a `property` called `greeting` that is initialized with a constant value.
3. `:::py def -> None:`
    - Represents the main method of this `flow`, which, when called, prints the value of the `greeting` property.

The `fy` tool automatically generates Python code from this flow definition.

## Generated Python Code
```py linenums="1"
from base.execution_flow_base import ExecutionFlowBase
from mixins.property.greeting.using_constant import Greeting_UsingConstant_PropertyMixin

class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Base
    ExecutionFlowBase[None]
):
    def __call__(self) -> None:
        print(self._greeting)

```
## Breakdown
1. `imports`
    - `fy` takes care of user specified, and generated imports.
2. `:::py Greeting_UsingConstant_PropertyMixin`
    - This mixin provides the logic to handle the `greeting` property, initialized as a constant.
3. `:::py ExecutionFlowBase[None]`
    - The base class for _flow_, with `None` as a return type.
4. `:::py self._greeting`
    - Flow's main behavior.

## Summary
In `fy`, defining a property in a flow allows you to encapsulate data as an attribute that can be used within the flow's methods. A property can be set with specific behavior, such as being a constant, ensuring that its value remains consistent throughout the flow's execution. This makes it easy to manage state and logic in a modular and intuitive way.