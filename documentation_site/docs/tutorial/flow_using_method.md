# Using Method in Flow
In this section, you'll learn how to use methdos withing the flow. We'll expand the "Hello World" example by adding a method to the flow.
## Syntax
```fy linenums="1"
flow HelloWorld:
    method greet using constant

    def -> None:
        self._greet()

```

## Breakdown of Syntax

1. `flow HelloWorld:`
    - Declares a `flow` named HelloWorld.
2. `method greet using constant`
    - Declares a `method` named `greet` that uses a constant implementation.
3. `def -> None:`
    - Begins the definition of a `method` that triggers the greet method.
4. `self._greet()`
    - Calls the `_greet` method to execute its functionality.


## Conversion to Python

The _Execution Flow_ tool generates the following Python code:
```py linenums="1"
from base.execution_flow_base import ExecutionFlowBase

from mixins.method.greet.using_constant import Greet_UsingConstant_MethodMixin


class HelloWorld_Flow(
    # Method Mixins
    Greet_UsingConstant_MethodMixin,
    # Base
    ExecutionFlowBase[None]
):
    def __call__(self) -> None:
        self._greet()

```
## Breakdown
1. `Greet_UsingConstant_MethodMixin`
    - Implements the `_greet` method with a constant (More in the [_Method Reference_](/reference/method)).
2. `__call__`
    - Executes the flow, calling the `_greet` method.

## Using Generated Code

```py
flow_instance = HelloWorld_Flow()
flow_instance()
```