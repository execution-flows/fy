# Property & Abstract Property

## What are properties?
`Execution Flow (fy)` properties allow you to define flow attributes that can be accessed in a controlled manner. These properties can either be abstract or implemented returning a constant or computed value.
## Abstract Properties
An abstract property in `fy` is a property that is defined but not implemented. Abstract properties are exclusively used by base flows, methods, and other properties. The abstract property is the way for a base flow, method, or other property to request from a flow to provide the implementation of the abstract property.

### Example
```fy title="Abstract Property" linenums="1"
property greeting: str
```
### Breakdown of Syntax
1. `property greeting: str`
    - Declares an abstract property named `greeting` with a return type of `str`.
    - Forces any subclass to implement this property, ensuring the flow can provide the required data.
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
1. `class With_Greeting_PropertyMixin_ABC(abc.ABC):`
    - Defines a mixin class that inherits from `abc.ABC`, making it an abstract base class. 
2. `@property`
    - Marks `_greeting` as a property, meaning it can be accessed like an attribute.
3. `@abc.abstractmethod`
    - Designates `_greeting` as an abstract method, requiring implementation in any subclass.
4. `raise NotImplementedError()`
    - Ensures that if `_greeting` is accessed without an implementation in a subclass, an error is raised.

## Property

```fy title="Property" linenums="1"
property greeting using constant:
    def -> str:
        return "Hello world!"
```

### Breakdown of Syntax
1. `property greeting using constant:`
    - Declares a simple property named `greeting` that returns a value of type `str`.
2. `def -> str:`
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
1. `class Greeting_UsingConstant_PropertyMixin:`
    - Defines a mixin class that includes the simple property.
2. `@property`
    - Indicates that `_greeting` is a property, accessed like an attribute.
3. `def _greeting(self) -> str:`
    - Implements the property, returning the string `"Hello world!"`.

## Usage in Execution Flow
Both abstract properties and properties in Execution Flow are designed to encapsulate data or computations, making managing and accessing the information within your flows easier. Abstract properties enforce consistent implementation across subclasses, while properties provide a direct way to return constant or computed values.