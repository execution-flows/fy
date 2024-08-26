## Execution Flows Development Paradigm

The evolution of programming languages has largely focused on improving code reusability. Initially, procedural languages provided the ability to organize code into subroutines or functions. This approach is straightforward: supply the function with the necessary data, invoke it, and gather the results. The same function can be reused across different data sets, making it a simple yet powerful tool.

[Object-Oriented Programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming) was the next major paradigm shift, where data and the functions that process it are encapsulated together in objects. This approach fosters code reusability by allowing data and behavior to coexist within objects. Following OOP, [Functional Programming (FP)](https://en.wikipedia.org/wiki/Functional_programming) emerged, elevating functions to first-class citizens. In FP, functions are treated like objects, allowing us to pass, return, and manipulate them, often with data bundled closely together via closures and similar constructs.

However, as software systems grow in complexity, especially with expanding use cases, the limitations of OOP and FP become apparent. While these paradigms provide powerful tools for code reuse, they often fall short. Developers still resort to code duplication or create abstractions that can limit flexibility and hinder future expansion.

[Design patterns](https://en.wikipedia.org/wiki/Design_Patterns) offer structured solutions for code reuse, but they, too, suffer from the same pitfalls. Patterns and abstractions inherently reduce the potential for functional variation, making codebases less adaptable to change. As a result, premature abstraction can stifle a project's ability to evolve rapidly. This is why early-stage startups often favor code duplication over abstraction—it’s quicker to copy, modify, and move forward.

Yet, delaying abstraction often means it never happens. Refactoring and rewriting become costly, non-functional endeavors that organizations are reluctant to undertake. So, how can we achieve highly reusable code without the constraints imposed by traditional abstractions?

The solution lies in creating code that is both modular and versatile, allowing for execution in various contexts without the limitations of rigid abstractions. OOP and FP provide mechanisms for combining data and behavior. Still, they struggle when we need to decompose code into its smallest units—down to individual lines or even parts of lines. At this level, managing the sheer number of classes and functions becomes unfeasible.

The challenge is not that OOP and FP are inadequate but that the current tools are ill-equipped to manage the vast number of granular components required for such flexibility. The size of classes and functions is dictated by two factors: how many you can write and how easily you can find the one you need.

This is where the Execution Flows paradigm comes into play. It offers a solution for managing the myriad OOP and FP building blocks necessary to support extensive use-case variation. By enabling the fine-grained control and composition of code, _Execution Flows_ empowers developers to create adaptable, reusable software without the constraints of traditional abstractions.

## Execution Flows Paradigm Explained

The strength of the _Execution Flows_ paradigm lies in its simplicity, centering around just three core entities: _flows_, _methods_, and _properties_. _Flows_ define a single use-case implementation in its entirety, utilizing _properties_ and _methods_ to achieve this. _Properties_ supply data, while _methods_ provide actions.

### Flows

A _flow_ is a callable entity that takes no arguments and can optionally return a value. For instance, the following function qualifies as a _flow_:

```py
def func() -> None:
    pass
```

Later, when we delve into advanced _Execution Flows_ concepts, we will explore why this definition is significant and how it facilitates various use cases.

In the context of the _fy_ tool, a _flow_ is a callable class that inherits from the `FlowBase` class and implements a `:::py def __call__(self) -> <return type>:` _method_. _Flows_ determine which implementations of _properties_ and _methods_ are used for the specific use case they address.

Here’s an example of a _fy_ flow that greets the user and returns no value:
```py
flow HelloWorld -> None:
    property greeting using hello_world
    method greet using greeting
```
### Methods and Properties

In the _Execution Flows_ paradigm, a _method_ is a mixin class that defines a single _method_. This _method_ can take arguments and optionally return a value. Similarly, a _property_ is a mixin class that defines a single _property_, annotated with Python's `:::py @property` decorator.

It’s essential to distinguish between abstract _methods_ or _properties_ and their concrete implementations.

### Abstract Methods and Properties

An _abstract method_ is declared by its name, arguments, and return value:

```py
method greet(greeting: str) -> None:
```
Similarly, the _abstract property_ is defined by its name and type.

```py
property greeting: str
```
These declarations simply announce the existence of a _property_ or _method_ so they can be referenced in the implementations of other _methods_ or _properties_.

### Method and Properties Implementation

To define a _method_ or _property_ implementation, just add a keyword using followed by the implementation name, like so:

```py
method greet(greeting: str) -> None using greeting:
```

Hosting flows utilize a specific implementation of a _property_ or _method_ by referencing its implementation name.

### Methods and properties using other methods and properties

When a _method_ requires other _methods_ or _properties_ to function, it declares these dependencies as mixins. For example, in the previous flow, the `greet` _method_ depends on the `greeting` _property_. The following fy code defines the `greet` _method_ implementation using the `greeting` _property_:

```py
method greet(greeting: str) -> None using greeting:
    with property greeting
```

This code signals to the hosting flow that it must provide an implementation for the `greeting` _property_.

Unlike _methods_, _properties_ can only utilize other _properties_ in their computations.

The "Tutorial" chapter provides more details on what development using the _fy_ tool looks like.
