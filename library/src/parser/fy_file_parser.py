# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import re
from pathlib import Path
from typing import List

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind, ParsedFlowFyFile, ParsedPropertyFyFile, \
    ParsedAbstractPropertyFyFile, ParsedAbstractMethodFyFile, ParsedMethodFyFile
from domain.python_entity_name import PythonEntityName
from domain.template_models import FlowTemplateModel, AbstractPropertyTemplateModel, PropertyTemplateModel, \
    PropertyMixinModel, AbstractMethodTemplateModel, MethodTemplateModel, MethodMixinModel

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
        re.MULTILINE
    )
    abstract_property_match_regex = re.compile(
        rf"^property\s+{FY_ENTITY_REGEX_STRING}\s*:\s*{PYTHON_MULTI_ENTITY_REGEX_STRING}\s*$",
        re.MULTILINE
    )
    property_match_regex = re.compile(
        rf"^property\s+{FY_ENTITY_REGEX_STRING}\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
        re.MULTILINE
    )

    abstract_method_match_regex = re.compile(
        rf"^method\s+{FY_ENTITY_REGEX_STRING}\s*(\({PYTHON_ARGUMENTS_REGEX_STRING}\))?"
        rf"\s*->\s*{PYTHON_MULTI_ENTITY_REGEX_STRING}\s*$",
        re.MULTILINE
    )

    method_match_regex = re.compile(
        rf"^method\s+{FY_ENTITY_REGEX_STRING}\s+using\s+{FY_ENTITY_REGEX_STRING}\s*:\s*$",
        re.MULTILINE
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    if re.match(flow_match_regex, fy_file_content):
        return ParsedFyFileKind.FLOW
    elif re.match(abstract_property_match_regex, fy_file_content):
        return ParsedFyFileKind.ABSTRACT_PROPERTY
    elif re.match(property_match_regex, fy_file_content):
        return ParsedFyFileKind.PROPERTY
    elif re.match(abstract_method_match_regex, fy_file_content):
        return ParsedFyFileKind.ABSTRACT_METHOD
    elif re.match(method_match_regex, fy_file_content):
        return ParsedFyFileKind.METHOD

    raise ValueError(f"Undetected file type for {file_path}")


def parse_flow_fy_file(file_path: Path) -> ParsedFyFile:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()

    flow_file_split = re.split(rf"flow\s+(?P<flow_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n", fy_file_content)
    flow_fy_search_name = flow_file_split[1]

    assert len(flow_file_split) == 3, f"Flow file length {len(flow_file_split)} is invalid."

    mixins_body_split_regex = re.compile(rf"\s+def\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n")
    mixins_body_split = mixins_body_split_regex.split(
        flow_file_split[-1]
    )
    flow_body = mixins_body_split[2]
    return_type = mixins_body_split[1]

    assert len(mixins_body_split) == 3, f"Flow file length {len(mixins_body_split)} is invalid."

    properties: List[PropertyMixinModel] = []
    methods: List[MethodMixinModel] = []
    mixin_lines = mixins_body_split[0].split('\n')
    for mixin_line in mixin_lines:
        if mixin_line == "":
            continue

        flow_property_regex = re.compile(
            rf"^\s+property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )
        flow_property_fy_search = re.search(flow_property_regex, mixin_line)
        if flow_property_fy_search:
            properties.append(PropertyMixinModel(
                property_name=PythonEntityName.from_snake_case(flow_property_fy_search.group("property_name")),
                implementation_name=PythonEntityName.from_snake_case(
                    flow_property_fy_search.group("implementation_name")),
                )
            )
        flow_method_regex = re.compile(
            rf"^\s+method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
            rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*$"
        )
        flow_method_fy_search = re.search(flow_method_regex, mixin_line)

        if flow_method_fy_search:
            methods.append(MethodMixinModel(
                method_name=PythonEntityName.from_snake_case(flow_method_fy_search.group("method_name")),
                implementation_name=PythonEntityName.from_snake_case(flow_method_fy_search.group("implementation_name")),
                )
            )

    parsed_fy_file = ParsedFlowFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=FlowTemplateModel(
            flow_name=PythonEntityName.from_pascal_case(flow_fy_search_name),
            python_class_name=PythonEntityName.from_pascal_case(f"{flow_fy_search_name}_Flow"),
            properties=properties,
            methods=methods,
            return_type=return_type,
            flow_call_body=flow_body,
        )
    )

    return parsed_fy_file


def parse_abc_property_fy_file(file_path: Path) -> ParsedFyFile:
    abstract_property_fy_regex = re.compile(
        rf"^property\s+(?P<abstract_property_name>{FY_ENTITY_REGEX_STRING})"
        r"\s*:\s*"
        rf"(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        re.MULTILINE
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        abstract_property_fy_search = abstract_property_fy_regex.search(fy_file_content)
    assert abstract_property_fy_search is not None, f"File {file_path} is invalid abstract property fy file."

    abstract_property_name_fy_search = abstract_property_fy_search.group("abstract_property_name")

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
            return_type=abstract_property_fy_search.group("return_type"),
        )
    )

    return parsed_fy_file


def parse_property_fy_file(file_path: Path) -> ParsedFyFile:
    property_fy_regex = re.compile(
        rf"^property\s+(?P<property_name>{FY_ENTITY_REGEX_STRING})\s+"
        rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        rf"\s+def\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n"
        r"(?P<property_body>.*)",
        re.DOTALL
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        property_fy_search = property_fy_regex.search(fy_file_content)
    assert property_fy_search is not None, f"File {file_path} is invalid property fy file"

    property_name_fy_search = property_fy_search.group("property_name")
    property_name = PythonEntityName.from_snake_case(property_name_fy_search)
    implementation_name = PythonEntityName.from_snake_case(property_fy_search.group("implementation_name"))

    parsed_fy_file = ParsedPropertyFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=PropertyTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{property_name.pascal_case}_Using{implementation_name.pascal_case}_PropertyMixin"
            ),
            property_name=property_name,
            implementation_name=implementation_name,
            return_type=property_fy_search.group("return_type"),
            property_body=property_fy_search.group("property_body"),
        )
    )
    return parsed_fy_file


def parse_abc_method_fy_file(file_path: Path) -> ParsedFyFile:
    abstract_method_fy_regex = re.compile(
        rf"^method\s+(?P<abstract_method_name>{FY_ENTITY_REGEX_STRING})"
        rf"\s*(\((?P<arguments>{PYTHON_ARGUMENTS_REGEX_STRING})\))?"
        rf"\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*$",
        re.MULTILINE
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        abstract_method_fy_search = abstract_method_fy_regex.search(fy_file_content)

    assert abstract_method_fy_search is not None, f"File {file_path} is invalid abstract method fy file"

    abstract_method_name_fy_search = abstract_method_fy_search.group("abstract_method_name")
    abstract_method_name = PythonEntityName.from_snake_case(abstract_method_name_fy_search)

    parsed_fy_file = ParsedAbstractMethodFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=AbstractMethodTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{abstract_method_name.pascal_case}_MethodMixin_ABC"
            ),
            abstract_method_name=abstract_method_name,
            arguments=abstract_method_fy_search.group("arguments"),
            return_type=abstract_method_fy_search.group("return_type")
        )
    )
    return parsed_fy_file


def parse_method_fy_file(file_path: Path) -> ParsedFyFile:
    method_fy_regex = re.compile(
        rf"^method\s+(?P<method_name>{FY_ENTITY_REGEX_STRING})\s+"
        rf"using\s+(?P<implementation_name>{FY_ENTITY_REGEX_STRING})\s*:\s*\n"
        rf"\s+def\s*(\((?P<arguments>{PYTHON_ARGUMENTS_REGEX_STRING})\))?"
        rf"\s*->\s*(?P<return_type>{PYTHON_MULTI_ENTITY_REGEX_STRING})\s*:\s*\n"
        rf"(?P<method_body>.*)",
        re.DOTALL
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        method_fy_search = method_fy_regex.search(fy_file_content)

    assert method_fy_search is not None, f"File {file_path} is invalid method fy file"

    implementation_name_fy_search = method_fy_search.group("implementation_name")
    implementation_name = PythonEntityName.from_snake_case(implementation_name_fy_search)
    method_name_fy_search = method_fy_search.group("method_name")
    method_name = PythonEntityName.from_snake_case(method_name_fy_search)

    parsed_fy_file = ParsedMethodFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=MethodTemplateModel(
            python_class_name=PythonEntityName.from_pascal_case(
                f"{method_name.pascal_case}_Using{implementation_name.pascal_case}_MethodMixin"
            ),
            method_name=method_name,
            arguments=method_fy_search.group("arguments"),
            return_type=method_fy_search.group("return_type"),
            method_body=method_fy_search.group("method_body"),
            implementation_name=PythonEntityName.from_snake_case(method_fy_search.group("implementation_name")),
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
