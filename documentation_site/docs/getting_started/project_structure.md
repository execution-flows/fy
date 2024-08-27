# Recommended Project Structure

Here's the recommended structure of a project utilizing the ___fy___ tool:

```
├── <project directory>
│   ├── src
│   │   ├── flows
│   │   │   ├── main_flow_fy.py
│   │   ├── mixins
│   │   │   ├── method
│   │   │   │   ├── greet
│   │   │   │   │   ├── using_hello_world_fy.py
│   │   │   ├── property
│   │   │   │   ├── greeting
│   │   │   │   │   ├── abc_fy.py
│   │   │   │   │   ├── greeting_fy.py
├── fy
│   ├── cli
│   │   ├── src
│   │   ...
│   ├── fy.sh
```

### Python Package for Flows

The `flows` package contains all flow-related files. Each file must end with the suffix `_fy.py`.

### Python Package for Mixins

The `mixins` package is organized into two sub-packages:

- **Method Mixins:** Contains directories and files related to method mixins. Files in this sub-package must end with `_fy.py`. For example an implementation of the method `greet` is located under `mixins/method/greet/` and is named by its implementation name - `using_hello_world_fy.py`.

- **Property Mixins:** Contains directories and files related to property mixins. Files in this sub-package must also end with `_fy.py`. For example, `abc_fy.py` and `greeting_fy.py` are located under `mixins/property/greeting/`.

This structure ensures that flow files and mixin files are consistently named and organized, making the project easier to manage and navigate.

### More granular split for large projects

While this is the recommended directory structure, larger projects with hundreds of flows and mixins require a more granular approach. This can involve a horizontal or vertical split.

A horizontal split follows the application layers, such as API, business logic, ORM or data access layer, third-party integrations, and similar application layers.

A vertical split divides the structure across domain boundaries, such as authentication, authorization, organization, different domain spaces, payment and billing, reporting, and similar domains.

For large projects, the most effective approach is to combine both methods: first, apply a horizontal split by application layer, then within each layer, apply vertical splits across domain lines.
