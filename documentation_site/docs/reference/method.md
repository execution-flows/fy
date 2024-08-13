# Method & Abstract Method

## What are Methods?
_Execution Flow (fy)_ methods are functions defined within flows that perform actions or calculations. These methods can be abstract, where they are declared but not implemented, or they can be implemented with specific behavior.

## Abstract Method Implementation
An _abstract method_ in `fy` is a method that is declared but not implemented. _Abstract methods_ are used by base flows to require that hosting flows provide their specific implementation. This ensures that the method is defined in any flow that inherits from the base flow.

### Example
```fy title="Abstract Method" linenums="1"
method greet(greeting: str) -> None
```


### Breakdown of Syntax
1. `:::py method greet(greeting: str) -> None`
    - Declares an abstract method named `greet` that takes a `greeting` parameter of type `str` and returns `None`.
    - Forces the hosting flow to implement this method, ensuring it is available to any code that needs it.

### Conversion to Python
```py linenums="1"
import abc

class Greet_MethodMixin_ABC(abc.ABC):
    @abc.abstractmethod
    def _greet(self, greeting: str) -> None:
        raise NotImplementedError()
```
### Breakdown
1. `:::py class Greet_MethodMixin_ABC(abc.ABC):`
    - Defines a mixin class that inherits from abc.ABC, making it an abstract base class.
2. `:::py @abc.abstractmethod`
    - Designates `_greet` as an abstract method, forcing the _hosting flow_ to provide an implementation.
3. `:::py raise NotImplementedError()`
    - Ensures that if `_greet` is called without an implementation, an error is raised.
## Method Implementation
```fy title="Method" linenums="1"
method greet using constant:
    def -> None:
        print("Hello World!")
```
### Breakdown of Syntax
1. `:::py method greet using constant:`
    - Declares a method named `greet` that is implemented using a constant behavior. Note that constant is not a keyword but an implementation name.
        - Some examples of implementations can be: `using db_record` or `using custom_behavior`.
2. `:::py def -> None:`
    - Begins the definition of the method, which returns `None`. 
    - `:::py print("Hello World!")` is the action performed by the method when it is called.

### Conversion to Python
```py linenums="1"
class Greet_UsingConstant_MethodMixin:
    def _greet(self) -> None:
        print("Hello World!")
```
### Breakdown
1. `:::py class Greet_UsingConstant_MethodMixin:`
    - Defines a _mixin class_ that includes the method implementation.
2. `:::py def _greet(self) -> None:`
    - Implements the method, printing `Hello World!` when called.

## Usage in Execution Flow
Both _abstract methods_ and _methods_ in _Execution Flow_ are designed to encapsulate behavior or actions within your flows. _Abstract methods_ enforce consistent implementation across flows, while methods provide a direct way to execute specific actions.