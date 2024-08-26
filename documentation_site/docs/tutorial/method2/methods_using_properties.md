# Integrating Properties with Methods in Execution Flows

In _Execution Flows_, properties and methods are core features that work together seamlessly to create modular and maintainable code. Methods can directly utilize properties within their implementations, allowing you to define methods that operate based on predefined properties, thereby enhancing the flexibility and power of your code.

## Example

Let's walk through how you can define a method that leverages a property, focusing on the structure and the corresponding Python code generated.

#### Implementing a Flow
Consider the following _Execution Flows_ setup, where a `greeting` _property_ is defined as a constant and a `greet` _method_ uses this property:
```py linenums="1"
"""fy
method greet -> None using greeting:
    with property greeting
"""

import abc

from fy_py_files.test_fy_py_files.flow_using_method_and_property_mixins.abc_fy import (
    With_Greeting_PropertyMixin_ABC,
)


# fy:start <<<===
class Greet_UsingGreeting_MethodMixin(
    # Property Mixins
    With_Greeting_PropertyMixin_ABC,
    abc.ABC,
):
    def _greet(self) -> None:
        # fy:end <<<===
        print(self._greeting)
```
### Breakdown
1. `:::py method greet -> None using greeting:`
    - **Method Declaration:** Defines a new method named `:::py greet`.
    - **Return Type:** `:::py -> None` specifies that the method does not return any value. 
    - **Using Property:** `:::py using greeting` indicates that the method will utilize the `:::py greeting` property.
2. `:::py with property greeting`
    - **Property Usage:** Specifies that the method will work with the `:::py greeting` property, which should be defined in the mixin.
3. Code Generation:
    - **Automatic Code Generation:** The `fy` tool generates code between `:::py # fy:start` and `:::py # fy:end`, including the class definition and the method implementation. 
    - **Imports:** Includes necessary imports, such as `:::py With_Greeting_PropertyMixin_ABC`, which contains the `:::py greeting` property, and `:::py abc.ABC` for abstract base class functionality.
4. Class Greet_UsingGreeting_MethodMixin 
    - **Base Class:** Inherits from With_Greeting_PropertyMixin_ABC and abc.ABC. This setup ensures that the class has the greeting property and can be used as an abstract class. 
    - **Method Implementation:** The `:::py _greet` method is defined to print the value of the `:::py _greeting` property, demonstrating how the method utilizes the property.

### Summary

This detailed tutorial illustrates how _Execution Flows_ enables seamless integration of properties with methods. By allowing methods to utilize properties, you can create dynamic, reusable, and modular code. The generated Python code maintains a clean separation of concerns, with properties and methods organized into mixins, ensuring that your code is both powerful and maintainable. This approach allows you to build complex logic while keeping your codebase organized and consistent.
