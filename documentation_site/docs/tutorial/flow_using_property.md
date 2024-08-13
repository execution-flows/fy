# Using Property in a Flow
We will now take a look into the next _Execution Flows_ component - `property`. _Property_ in _Execution Flows_ serves a purpose of providing data to the flow code. 
## Syntax

```fy linenums="1"
flow HelloWorld:
    property greeting using constant

    def -> None:
        print(self._greeting)

```

## Breakdown of Syntax
1. `flow HelloWorld:`
    - Declares a flow
2. `:::py property greeting using constant`
    - Declares a property named `greeting` that returns a constant value.
3. `:::py self._greeting` 
    - The Python implementation of the `greeting` property.

## Conversion to Python
The _Execution Flow_ tool generates following Python code.
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
1. `:::py Greeting_UsingConstant_PropertyMixin`
    - _Property_ that returns `str` (More in the [_Property Reference_](/reference/Property/property) chapter)
2. `:::py __call__`
    - Executes the flow, printing the value of `_greeting` property.

This tutorial demonstrates how to declare and use _Property_ within the hosting flow, showcasing the power of properties in making your code modular.
