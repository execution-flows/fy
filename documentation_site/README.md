## Installation

- It should be installed once you run `poetry install`
## Setting up versioning 
  - We are using `mike` for versioning 
### Building up docs
```shell
mike deploy --push --update-aliases <version_tag> latest
```
### Setting up latest as a default version
```shell
mike set-default --push latest
```
## Usage 

- To start `mike serve` 
```shell
mkdocs serve
```
- Address will be listed in terminal. For example `http://127.0.0.1:8000/`.
