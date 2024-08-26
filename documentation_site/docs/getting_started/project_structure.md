The `fy` tool's project structure is organized into specific packages and directories to maintain clarity and ease of use. Here's an overview:

### Directory Structure
```
├── fy
│   ├── flows
│   │   ├── main_flow_fy.py
│   │   ├──mixins
│   │   │   ├── method
│   │   │   │   ├── greet
│   │   │   │   │   ├── using_hello_world_fy.py
│   │   │   ├── property
│   │   │   │   ├── greeting
│   │   │   │   │   ├── abc_fy.py
│   │   │   │   │   ├── greeting_fy.py
├── local-fy-cli
│   ├── cli
│   ├── documentation_site
│   ├── library
│   ├── local.fy.sh
```

### Python Package for Flows

The `flows` package contains all flow-related files. Each file must end with the suffix `_fy.py`, as illustrated by `main_flow_fy.py`.

### Python Package for Mixins

The `mixins` package is organized into two sub-packages:

- **Method Mixins:** Contains mixins related to methods. Files in this sub-package must end with `_fy.py`. For example, `using_hello_world_fy.py` is located under `mixins/method/greet/`.

- **Property Mixins:** Contains mixins related to properties. Files in this sub-package must also end with `_fy.py`. For example, `abc_fy.py` and `greeting_fy.py` are located under `mixins/property/greeting/`.

This structure ensures that flow files and mixin files are consistently named and organized, making the project easier to manage and navigate.
