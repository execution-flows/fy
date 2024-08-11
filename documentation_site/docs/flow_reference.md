# "Hello World!" Flow

## Hello World Example

The `Execution Flow (fy)` tool enables developers to achieve a high level of code reusability by generating object-oriented Python code using a unique 
syntax that simplifies the construction of Python code. Below is a step-by-step guide to creating a simple "Hello World"
program using `Execution Flow`.

```py linenums="1"
flow HelloWorld:
    def -> None:
        print("Hello world!")

```

##  Breakdown of Syntax
1. `flow HelloWorld:` :
    - This line declares a new flow, which is essentially a class in Python. The name `HelloWorld` is the identifier for 
         this flow.
2. `def -> None:`
    - This line starts the definition of the function to be executed within the flow.
    - Syntax: 
        - `def` indicates the beginning of the function definiton
        - `None` specifies return type (In this example no return type)
3. `print("Hello world!")`
    - Actual operation performed by the function

## Conversion to Python
When this flow is processed by `Execution Flow` tool, it generates the following Python code:

```py hl_lines="1 4" linenums="1"
from base.execution_flow_base import ExecutionFlowBase


class HelloWorld_Flow(ExecutionFlowBase[None]):
    def __call__(self) -> None:
        print("Hello world!")

```

## Breakdown
1. `from base.execution_flow_base import ExecutionFlowBase`
   - Essential for the flow's functionality
2. `class HelloWorld_Flow(ExecutionFlowBase[None]):`
   - Defines Python class, and return type of ExecutionFlowBase
3. `def __call__(self) -> None:`
   - Entry point of the flow when it is executed
4. `print("Hello world!")`
   - Actual operation performed by the function

## How to use
Once the `Execution Flow` tool has generated the Python code, you can execute the flow in your Python environment.

```py
flow_instance = HelloWorld_Flow()
flow_instance()
```

If everything was done correctly expected output should be `Hello world!`.