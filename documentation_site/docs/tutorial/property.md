# Using Properties in a Flow
We will expand on our knowledge of `Execution Flows` by adding `Property`. In our `flow` we will introduce `property` to print greeting message.

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
2. `property greeting using constant`
    - Declares a property named `greeting` that returns a constant value.

## Conversion to Python
The `Execution Flow` tool generates following Python code.
```py linenums="1"
from base.execution_flow_base import ExecutionFlowBase

from tests.test_fy_files.hello_world_using_property import Greeting_UsingConstant_PropertyMixin


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
1. `Greeting_UsingConstant_PropertyMixin`
    - `Property` that returns `str` (more in the `Property` chapter)
2. `__call__`
    - Executes the flow, printing the value of `_greeting` property.

This tutorial demonstrates how to declare and use property within the hosting flow, showcasing the power of properties in making your code modular.
