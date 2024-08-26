In Execution Flow (fy), setters can be used in conjunction with abstract properties to manage and control how values are assigned. Setters can be written manually, just like any other property. Or, the `fy` tool can generate the necessary boilerplate code for you.

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
