# Integrating Properties with Methods in Execution Flows

In _Execution Flows_, properties and methods are core features that work together seamlessly to create modular and maintainable code. Methods can directly utilize properties within their implementations, allowing you to define methods that operate based on predefined properties, thereby enhancing the flexibility and power of your code.

## Example

Let's walk through how you can define a method that leverages a property, focusing on the structure and the corresponding Python code generated.

#### Implementing a Flow

Consider the following _Execution Flows_ setup, where a `greeting` _property_ is defined as a constant and a `greet` _method_ uses this property:

=== "fy"
    ```fy
    method greet -> None using greeting:
        with property greeting
    ```

=== "Python"

    ```py title="mixins/method/greet/using_greeting_fy.py" linenums="1"
    """fy
    method greet -> None using greeting:
        with property greeting
    """
    
    import abc
    
    from mixins.property.greeting.abc_fy import (
        With_Greeting_PropertyMixin_ABC,
    )
    
    
    # fy:start ===>>>
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
    - **Method Declaration:** Defines an implementation of a method named `:::py greet`.
    - **Return Type:** `:::py -> None` specifies that the method does not return any value.
    - **Implementation Name:** `:::py using greeting` defines the implementation name that is then referenced by the hosting flow when included in a flow. ==Note that `greeting` in `using greeting` is not correlated with `greeting` in `with property greeting`. The former can be any arbitrary name and defines the method implementation name. The second is a reference to an existing abstract property in the project.==
2. `:::py with property greeting`
    - **Property Usage:** Specifies that the method will use the `:::py greeting` property in its implementation.
3. Code Generation:
    - **Automatic Code Generation:** The ___fy___ tool generates code between `:::py # fy:start` and `:::py # fy:end` including the class definition and the method declaration. 
    - **Imports:** Includes necessary imports, such as `:::py With_Greeting_PropertyMixin_ABC`, which contains the `:::py greeting` property, and `:::py abc.ABC` for abstract base class functionality.
4. Class `:::py Greet_UsingGreeting_MethodMixin` 
    - **Base Class:** Inherits from `:::py With_Greeting_PropertyMixin_ABC` and `:::py abc.ABC`. This setup ensures that the class will have access to the `greeting` property implementation. 
    - **Method Implementation:** The `:::py _greet` method is defined to print the value of the `:::py _greeting` property, demonstrating how the method utilizes the property.

### Summary

This detailed tutorial illustrates how _Execution Flows_ enables seamless integration of properties with methods. By allowing methods to utilize properties, you can create dynamic, reusable, and modular code. The generated Python code maintains a clean separation of concerns, with properties and methods organized into mixins, ensuring that your code is both complex and maintainable. This approach allows you to build complex logic while keeping your codebase organized and consistent.
