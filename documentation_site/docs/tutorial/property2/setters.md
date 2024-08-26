When using the _Execution Flows_ `fy` tool, writing a property setter manually involves defining a property and then adding a `@<property_name>.setter` method to manage how the property value is assigned. Alternatively, the `fy` tool simplifies this process by generating the necessary boilerplate code. You can declare an abstract property and include `property <property_name> using setter` in the flow mixins, allowing the tool to automatically handle the setter implementation. This approach streamlines property management in your code.


## Automatically Generated Setter Implementation
When a flow declares a setter, the `fy` tool checks if an implementation for the defined property exists. If it does not find the implementation, it generates one. 

Below is an example of the generated code for a setter for the `property greeting: str`.
### Example
```py linenums="1"
"""fy
property greeting: str
"""

import abc


# fy:start <<<===
class With_Greeting_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _greeting(self) -> str:
        raise NotImplementedError()

    @_greeting.setter
    @abc.abstractmethod
    def _greeting(self, value: str) -> None:
        raise NotImplementedError()
        # fy:end <<<===
```
