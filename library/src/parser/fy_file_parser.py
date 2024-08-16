# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from pathlib import Path
from typing import List

from domain.parsed_fy_file import (
    ParsedFyFile,
    ParsedFyFileKind,
    ParsedFlowFyFile,
    ParsedPropertyFyFile,
    ParsedAbstractPropertyFyFile,
    ParsedAbstractMethodFyFile,
    ParsedMethodFyFile,
)
from domain.python_entity_name import PythonEntityName
from domain.template_models import (
    FlowTemplateModel,
    AbstractPropertyTemplateModel,
    PropertyTemplateModel,
    PropertyMixinModel,
    AbstractMethodTemplateModel,
    MethodTemplateModel,
    MethodMixinModel,
    AbstractPropertyModel,
    AbstractMethodModel,
)

PYTHON_ENTITY_CHAR_REGEX_STRING = r"[\w.\[\]]"
PYTHON_MULTI_ENTITY_REGEX_STRING = (
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}|"
    rf"{PYTHON_ENTITY_CHAR_REGEX_STRING}[\w.\[\]\s\|]*{PYTHON_ENTITY_CHAR_REGEX_STRING}"
)
PYTHON_ARGUMENTS_REGEX_STRING = r"\s*[^)]*\s*"
FY_ENTITY_REGEX_STRING = r"\w+"


def detect_fy_file_kind(file_path: Path) -> ParsedFyFileKind:
    flow_match_regex = re.compile(
        rf"^flow\s+{FY_ENTITY_REGEX_STRING}(\s+extends\s+{FY_ENTITY_REGEX_STRING})?\s*:\s*$",
    )
    abstract_property_match_regex = re.compile(
        rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*:\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
    )
    property_match_regex = re.compile(
        rf"^property\s+{FY_ENTITY_REGEX_STRING}\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
    )

    abstract_method_match_regex = re.compile(
        rf"^method\s+{FY_ENTITY_REGEX_STRING}\s*(\({PYTHON_ARGUMENTS_REGEX_STRING}\))?"
        rf"\s*->\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
    )

    method_match_regex = re.compile(
        rf"^method\s+{FY_ENTITY_REGEX_STRING}\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    for fy_line in fy_file_content.split("\n"):
        if flow_match_regex.match(fy_line) is not None:
            return ParsedFyFileKind.FLOW
        elif abstract_property_match_regex.match(fy_line) is not None:
            return ParsedFyFileKind.ABSTRACT_PROPERTY
        elif property_match_regex.match(fy_line) is not None:
            return ParsedFyFileKind.PROPERTY
        elif abstract_method_match_regex.match(fy_line) is not None:
            return ParsedFyFileKind.ABSTRACT_METHOD
        elif method_match_regex.search(fy_line) is not None:
            return ParsedFyFileKind.METHOD

    raise ValueError(f"Undetected file type for {file_path}")


def parse_flow_fy_file(file_path: Path) -> ParsedFyFile:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    flow_file_split_regex = re.compile(
        rf"flow\s+(?P<flow_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
    )

    flow_file_split = flow_file_split_regex.split(fy_file_content)

    assert (
        len(flow_file_split) == 3
    ), f"Flow file length {len(flow_file_split)} is invalid."

    user_imports = flow_file_split[0]
    flow_fy_search_name = flow_file_split[1]

    mixins_body_split_regex = re.compile(
        rf"\s+def\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n"
    )
    mixins_body_split = mixins_body_split_regex.split(flow_file_split[-1])
    flow_body = mixins_body_split[2]
    return_type = mixins_body_split[1]

    assert (
        len(mixins_body_split) == 3
    ), f"Flow file length {len(mixins_body_split)} is invalid."

    properties: List[PropertyMixinModel] = []
    methods: List[MethodMixinModel] = []
    mixin_lines = mixins_body_split[0].split("\n")
    for mixin_line in mixin_lines:
        if mixin_line.strip() == "":
            continue

        flow_property_regex = re.compile(
            pattern=rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )
        flow_property_fy_search = flow_property_regex.search(mixin_line)
        if flow_property_fy_search:
            properties.append(
                PropertyMixinModel(
                    property_name=PythonEntityName.from_snake_case(
                        flow_property_fy_search.group("property_name")
                    ),
                    implementation_name=PythonEntityName.from_snake_case(
                        flow_property_fy_search.group("implementation_name")
                    ),
                )
            )
        flow_method_regex = re.compile(
            pattern=rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )
        flow_method_fy_search = flow_method_regex.search(mixin_line)

        if flow_method_fy_search:
            methods.append(
                MethodMixinModel(
                    method_name=PythonEntityName.from_snake_case(
                        flow_method_fy_search.group("method_name")
                    ),
                    implementation_name=PythonEntityName.from_snake_case(
                        flow_method_fy_search.group("implementation_name")
                    ),
                )
            )

    parsed_fy_file = ParsedFlowFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=FlowTemplateModel(
            flow_name=PythonEntityName.from_pascal_case(flow_fy_search_name),
            python_class_name=PythonEntityName.from_pascal_case(
                f"{flow_fy_search_name}_Flow"
            ),
            properties=properties,
            methods=methods,
            return_type=return_type,
            flow_call_body=flow_body,
            user_imports=user_imports,
        ),
    )

    return parsed_fy_file


def parse_abc_property_fy_file(file_path: Path) -> ParsedFyFile:
    abstract_property_fy_regex = re.compile(
        rf"property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        r"\s*:\s*"
        rf"(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        abstract_property_fy_search = abstract_property_fy_regex.split(fy_file_content)

    user_imports = abstract_property_fy_search[0]
    abstract_property_name_fy_search = abstract_property_fy_search[1]

    abstract_property_name = PythonEntityName.from_snake_case(
        abstract_property_name_fy_search
    )
    parsed_fy_file = ParsedAbstractPropertyFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=AbstractPropertyTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"With_{abstract_property_name.pascal_case}_PropertyMixin_ABC"
            ),
            abstract_property_name=abstract_property_name,
            return_type=abstract_property_fy_search[2],
            user_imports=user_imports,
        ),
    )

    return parsed_fy_file


def parse_property_fy_file(file_path: Path) -> ParsedFyFile:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    property_file_split_regex = re.compile(
        rf"property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+using\s+"
        rf"(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
    )

    property_file_split = property_file_split_regex.split(fy_file_content)

    assert (
        len(property_file_split) == 4
    ), f"Property file length {len(property_file_split)} is invalid."

    user_imports = property_file_split[0]
    property_name = PythonEntityName.from_snake_case(property_file_split[1])
    implementation_name = PythonEntityName.from_snake_case(property_file_split[2])

    property_body_split_regex = re.compile(
        rf"\s+def\s*->\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n"
    )

    property_body_split = property_body_split_regex.split(property_file_split[-1])

    assert (
        len(property_body_split) == 3
    ), f"Property file length {len(property_body_split)} is invalid."

    return_type = property_body_split[1]
    property_body = property_body_split[2]

    abstract_properties: List[AbstractPropertyModel] = []

    abstract_property_mixin_regex = re.compile(
        rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
    )

    mixin_lines = property_body_split[0].split("\n")
    for mixin_line in mixin_lines:
        if mixin_line.strip() == "":
            continue

        declared_abstract_property_mixin = abstract_property_mixin_regex.search(
            mixin_line
        )

        if declared_abstract_property_mixin:
            abstract_properties.append(
                AbstractPropertyModel(
                    property_name=PythonEntityName.from_snake_case(
                        declared_abstract_property_mixin.group("abstract_property_name")
                    )
                )
            )

    parsed_fy_file = ParsedPropertyFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=PropertyTemplateModel(
            property_name=property_name,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
            ),
            implementation_name=implementation_name,
            abstract_property_mixins=abstract_properties,
            return_type=return_type,
            property_body=property_body,
            user_imports=user_imports,
        ),
    )
    return parsed_fy_file


def parse_abc_method_fy_file(file_path: Path) -> ParsedFyFile:
    abstract_method_fy_regex = re.compile(
        rf"method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
        rf"\s*(\((?P<arguments>{PYTHON_ARGUMENTS_REGEX_STRING})\))?"
        rf"\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        abstract_method_fy_search = abstract_method_fy_regex.split(fy_file_content)

    assert (
        len(abstract_method_fy_search) == 6
    ), f"Abstract method fy search is {abstract_method_fy_search} length."

    user_imports = abstract_method_fy_search[0]
    abstract_method_name_fy_search = abstract_method_fy_search[1]

    abstract_method_name = PythonEntityName.from_snake_case(
        abstract_method_name_fy_search
    )

    parsed_fy_file = ParsedAbstractMethodFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=AbstractMethodTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{abstract_method_name.pascal_case}_MethodMixin_ABC"
            ),
            abstract_method_name=abstract_method_name,
            arguments=abstract_method_fy_search[3],
            return_type=abstract_method_fy_search[4],
            user_imports=user_imports,
        ),
    )
    return parsed_fy_file


def parse_method_fy_file(file_path: Path) -> ParsedFyFile:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    method_file_split_regex = re.compile(
        rf"method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+using\s+"
        rf"(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
    )
    method_file_split = method_file_split_regex.split(fy_file_content)

    assert (
        len(method_file_split) == 4
    ), f"Method file length {len(method_file_split)} is invalid."

    user_imports = method_file_split[0]
    method_name = PythonEntityName.from_snake_case(method_file_split[1])
    implementation_name = PythonEntityName.from_snake_case(method_file_split[2])

    method_body_split_regex = re.compile(
        rf"\s+def\s*(\(({PYTHON_ARGUMENTS_REGEX_STRING})\))?\s*->\s*({PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n"
    )
    method_body_split = method_body_split_regex.split(method_file_split[-1])

    assert (
        len(method_body_split) == 5
    ), f"Method file length {len(method_body_split)} is invalid."

    arguments = method_body_split[2]
    return_type = method_body_split[3]
    method_body = method_body_split[4]

    abstract_properties: List[AbstractPropertyModel] = []
    abstract_methods: List[AbstractMethodModel] = []

    abstract_property_mixin_regex = re.compile(
        rf"^\s+with\s+property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
    )

    abstract_method_mixin_regex = re.compile(
        rf"^\s+with\s+method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
    )

    mixin_lines = method_body_split[0].split("\n")
    for mixin_line in mixin_lines:
        if mixin_line.strip() == "":
            continue

        declared_abstract_property_mixin = abstract_property_mixin_regex.search(
            mixin_line
        )
        declared_abstract_method_mixin = abstract_method_mixin_regex.search(mixin_line)
        if declared_abstract_property_mixin:
            abstract_properties.append(
                AbstractPropertyModel(
                    property_name=PythonEntityName.from_snake_case(
                        declared_abstract_property_mixin.group("abstract_property_name")
                    )
                )
            )

        if declared_abstract_method_mixin:
            abstract_methods.append(
                AbstractMethodModel(
                    method_name=PythonEntityName.from_snake_case(
                        declared_abstract_method_mixin.group("abstract_method_name")
                    )
                )
            )

    parsed_fy_file = ParsedMethodFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=MethodTemplateModel(
            method_name=method_name,
            python_class_name=PythonEntityName.from_pascal_case(
                f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
            ),
            implementation_name=implementation_name,
            abstract_property_mixins=abstract_properties,
            abstract_method_mixins=abstract_methods,
            arguments=arguments,
            return_type=return_type,
            method_body=method_body,
            user_imports=user_imports,
        ),
    )
    return parsed_fy_file


class FyFileParser:
    @staticmethod
    def parse(file_path: Path) -> ParsedFyFile:
        fy_file_kind = detect_fy_file_kind(file_path)
        match fy_file_kind:
            case ParsedFyFileKind.FLOW:
                return parse_flow_fy_file(file_path)
            case ParsedFyFileKind.ABSTRACT_PROPERTY:
                return parse_abc_property_fy_file(file_path)
            case ParsedFyFileKind.PROPERTY:
                return parse_property_fy_file(file_path)
            case ParsedFyFileKind.ABSTRACT_METHOD:
                return parse_abc_method_fy_file(file_path)
            case ParsedFyFileKind.METHOD:
                return parse_method_fy_file(file_path)
