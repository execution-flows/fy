# _Execution Flows_ Explained

The strength of the _Execution Flows_ paradigm comes from two key principles:

1. **Simplicity**: The ___fy___ implementation revolves around just three core entities: _flows_, _methods_, and _properties_. A _flow_ defines a particular use case by integrating _property_ and _method_ mixins into a single class. _Property_ mixins supply data, while _method_ mixins provide actions.
2. **Static referencing**: Flows, methods, and properties can only use other flows, methods, or properties that they explicitly reference by their identifier.

## Static referencing

_Static referencing_ differs from _static typing_ in that it requires not only the type of the entity to match but also its identifier.

In traditional _static typing_ environment values are matched by its type. In the following example a function `greet` accepts any string.

```python
def hello_world() -> str:
    return "Hello, World!"

def greet(greeting: str) -> None:
    print(greeting)

greet(hello_world())
```

That means that we could also write something like:

```python
greet(datetime.utcnow().isoformat())
```

We cannot determine just by looking at the code whether this was an error or intentional.

Here’s an example of a ___fy___ flow with a related method and property that greets the user and returns no value.
