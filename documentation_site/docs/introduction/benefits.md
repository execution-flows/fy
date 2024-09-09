# A couple of non-obvious benefits

A flow class cannot be instantiated if it is missing a property or method implementation from the mixin list. Tools like `mypy` or `PyCharm` will report classes that are missing an abstract method or property implementation. The Python interpreter raises an exception if you try to instantiate such a class. These tools also identify which abstract method or property is missing its implementation, making it easy to fix the issue.

With this feature you get two benefits:

1. Issues are detected during static code analysis, which is much better than waiting to execute the code to discover the problem.
2. You do not need to worry if you forgot to include a property or mixin implementation. The tools will let you know.
