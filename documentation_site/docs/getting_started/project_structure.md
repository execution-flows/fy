Here's the recommended structure of a project managed by the `fy` tool:

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
├── local-fy-cli
│   ├── fy.sh
```

### Python Package for Flows

The `flows` package contains all flow-related files. Each file must end with the suffix `_fy.py`.

### Python Package for Mixins

The `mixins` package is organized into two sub-packages:

- **Method Mixins:** Contains directories and files related to method mixins. Files in this sub-package must end with `_fy.py`. For example an implementation of the method `greet` is located under `mixins/method/greet/` and is named by its implementation name - `using_hello_world_fy.py`.

- **Property Mixins:** Contains directories and files related to property mixins. Files in this sub-package must also end with `_fy.py`. For example, `abc_fy.py` and `greeting_fy.py` are located under `mixins/property/greeting/`.

This structure ensures that flow files and mixin files are consistently named and organized, making the project easier to manage and navigate.
