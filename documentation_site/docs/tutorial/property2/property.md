# What are properties?

`Execution Flow (fy)` properties allow you to define flow attributes that can be accessed in a controlled manner. These properties can either be abstract or implemented returning a constant or computed value.
## Abstract Property Implementation
An abstract property in `fy` is a property that is declared but not implemented. Abstract properties are exclusively used by base flows, methods, and other properties. The abstract property is the way for a base flow, method, or other property to request from a hosting flow to provide the implementation of the abstract property.

### Example
```fy title="Abstract Property" linenums="1"
property greeting: str
```
### Breakdown of Syntax
1. `:::py property greeting: str`
    - Declares an abstract property named `greeting` with a return type of `str`.
    - Forces the hosting flow to use the property implementation, ensuring the data is provided to any code using the property.
### Conversion to Python
```py linenums="1"
import abc

class With_Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()

```
### Breakdown
1. `:::py class With_Greeting_PropertyMixin_ABC(abc.ABC):`
    - Defines a mixin class that inherits from `abc.ABC`, making it an abstract base class. 
2. `:::py @property`
    - Marks `_greeting` as a property, meaning it can be accessed like an attribute.
3. `:::py @abc.abstractmethod`
    - Designates `_greeting` as an abstract method, the hosting flow to use a property implementation.
4. `:::py raise NotImplementedError()`
    - Ensures that if `_greeting` is accessed without an implementation, an error is raised.

## Property Implementation

```fy title="Property" linenums="1"
property greeting using constant:
    def -> str:
        return "Hello world!"
```

### Breakdown of Syntax
1. `:::py property greeting using constant:`
    - Declares a simple property named `greeting` that returns a constant value. Note that `constant` is not a keyword, but an implementation name. 
       - Some examples of implementations can be: `using db_record` or `using hour_of_day`.
2. `:::py def -> str:`
    - Begins the definition of the property method that returns a `str`.
    - `return "Hello world!` is the value that property returns when accessed.

### Conversion to Python

```py linenums="1"
class Greeting_UsingConstant_PropertyMixin:
   @property
   def _greeting(self) -> str:
        return "Hello world!"
```
### Breakdown 
1. `:::py class Greeting_UsingConstant_PropertyMixin:`
    - Defines a mixin class that includes the property implementation.
2. `:::py @property`
    - Indicates that `_greeting` is a property, accessed like an attribute.
3. `:::py def _greeting(self) -> str:`
    - Implements the property, returning the string `"Hello world!"`.

## Usage in Execution Flow
Both abstract properties and properties in Execution Flow are designed to encapsulate data or computations, making managing and accessing the information within your flows easier. Abstract properties enforce consistent implementation across flows, while properties provide a direct way to return constant or computed values.
