import re
from pathlib import Path
from typing import List

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind, ParsedFlowFyFile, ParsedPropertyFyFile, \
    ParsedAbstractPropertyFyFile
from domain.python_entity_name import PythonEntityName
from domain.template_models import FlowTemplateModel, AbstractPropertyTemplateModel, PropertyTemplateModel, \
    PropertyMixinModel


def detect_fy_file_kind(file_path: Path) -> ParsedFyFileKind:
    flow_match_regex = re.compile(
        r"^flow \w+( extends \w+)?:$",
        re.MULTILINE
    )
    abstract_property_match_regex = re.compile(
        r"^property \w+: [\w.]*$",
        re.MULTILINE
    )
    property_match_regex = re.compile(
        r"^property \w+ using \w+:$",
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


def parse_flow_fy_file(file_path: Path) -> ParsedFyFile:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        # flow_fy_search = flow_fy_regex.search(fy_file_content)
    flow_file_split = re.split(r"flow (?P<flow_name>\w+):\n", fy_file_content)
    flow_fy_search_name = flow_file_split[1]

    assert len(flow_file_split) == 3, f"Flow file length {len(flow_file_split)} is invalid."

    mixins_body_split = re.split(r"\s+def -> (?P<return_type>[\w.]+):\n", flow_file_split[-1])
    mixin_body = mixins_body_split[2]
    return_type = mixins_body_split[1]

    assert len(mixins_body_split) == 3, f"Flow file length {len(mixins_body_split)} is invalid."

    properties: List[PropertyMixinModel] = []
    mixin_lines = mixins_body_split[0].split('\n')
    for mixin_line in mixin_lines:
        if mixin_line == "":
            continue

        flow_property_regex = re.compile(
            "\s+property (?P<property_name>\w+) using (?P<implementation_name>\w+)"
                   )
        flow_property_fy_search = re.search(flow_property_regex, mixin_line)

        assert flow_property_fy_search, f"Invalid flow mixin {mixin_line}"

        properties.append(PropertyMixinModel(
            property_name=PythonEntityName.from_snake_case(flow_property_fy_search.group("property_name")),
            implementation_name=PythonEntityName.from_snake_case(flow_property_fy_search.group("implementation_name")),
        ))

    parsed_fy_file = ParsedFlowFyFile(
        input_fy_file_path=file_path,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=FlowTemplateModel(
            flow_name=PythonEntityName.from_pascal_case(flow_fy_search_name),
            python_class_name=PythonEntityName.from_pascal_case(f"{flow_fy_search_name}_Flow"),
            properties=properties,
            return_type=return_type,
            flow_call_body=mixin_body,
        )
    )

    return parsed_fy_file


def parse_abc_property_fy_file(file_path: Path) -> ParsedFyFile:
    abstract_property_fy_regex = re.compile(
        r"property (?P<abstract_property_name>\w+)"
        r": (?P<return_type>[\w.]+)"
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


def parse_property_fy_file(file_path: Path):
    property_fy_regex = re.compile(
        r"property (?P<property_name>\w+) using (?P<implementation_name>\w+):\n"
        r"\s+def -> (?P<return_type>[\w.]+):\n"
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
