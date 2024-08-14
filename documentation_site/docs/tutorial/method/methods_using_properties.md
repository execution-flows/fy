# Integrating Properties with Methods in Execution Flows

In _Execution Flows_, properties and methods are core features that work together seamlessly to create modular and maintainable code. Methods can directly utilize properties within their implementations, allowing you to define methods that operate based on predefined properties, thereby enhancing the flexibility and power of your code.

## Example

Let's walk through how you can define a method that leverages a property, focusing on the structure and the corresponding Python code generated.

#### Implementing a Flow
Consider the following _Execution Flows_ setup, where a `greeting` _property_ is defined as a constant and a `greet` _method_ uses this property:
```fy linenums="1"
flow HelloWorld_Flow:
    property greeting using constant
    method greet using greeting

    def -> None:
        self._greet()
```
### Method and Property Definitions
#### Implementing a method
The `greet` _method_ is defined to utilize the `greeting` _property_. Here’s how the method is structured:
```fy  linenums="1"
method greet using greeting:
    with property greeting

    def -> None:
        print(self._greeting)
```
1. `:::py with property greeting`

   - Specifies that this _method_ will use the `greeting` _property_ within its logic.
#### Implementing a property
```fy linenums="1"
property greeting using constant:
    def -> str:
        return "Hello world!"
```
#### Implementing a Abstract 
```fy title="Declaring a Abstract Property"
property greeting: str
```

### Generated Python Code
The _Execution Flow_ tool automatically converts the above definitions into Python classes and mixins. Here’s how the generated Python code looks.
#### Main Flow Class
```py linenums="1"
from base.execution_flow_base import ExecutionFlowBase
from tests.test_fy_files.both_mixins import Greeting_UsingConstant_PropertyMixin
from tests.test_fy_files.both_mixins import Greet_UsingGreeting_MethodMixin

class HelloWorld_Flow(
    # Property Mixins
    Greeting_UsingConstant_PropertyMixin,
    # Method Mixins
    Greet_UsingGreeting_MethodMixin,
    # Base
    ExecutionFlowBase[None]
):
    def __call__(self) -> None:
        self._greet()
```
#### Method Mixin
The _method_ `greet` is encapsulated in a mixin that ensures the method has access to the `greeting` _property_.
```py linenums="1"
import abc
from tests.test_fy_files.both_mixins import With_Greeting_PropertyMixin_ABC

class Greet_UsingGreeting_MethodMixin(
    # Property Mixins
    With_Greeting_PropertyMixin_ABC,
    abc.ABC
):
    def _greet(self) -> None:
        print(self._greeting) 
```
#### Property Mixin
The constant `greeting` _property_ is implemented in its own mixin.

```py linenums="1"
class Greeting_UsingConstant_PropertyMixin:
   @property
   def _greeting(self) -> str:
        return "Hello world!"
```

#### Abstract Property Mixin
The abstract base for the `greeting` _property_ is defined as follows.
```py linenums="1"
import abc

class With_Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()
```

### Summary

This detailed tutorial illustrates how _Execution Flows_ enables seamless integration of properties with methods. By allowing methods to utilize properties, you can create dynamic, reusable, and modular code. The generated Python code maintains a clean separation of concerns, with properties and methods organized into mixins, ensuring that your code is both powerful and maintainable. This approach allows you to build complex logic while keeping your codebase organized and consistent.