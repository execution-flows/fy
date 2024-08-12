import re
from pathlib import Path

from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind, ParsedFlowFyFile, ParsedPropertyFyFile, \
    ParsedAbstractPropertyFyFile
from domain.python_entity_name import PythonEntityName
from domain.template_models import FlowTemplateModel, AbstractPropertyTemplateModel, PropertyTemplateModel


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
        flow_fy_file = re.match(flow_match_regex, fy_file_content)
        abstract_property_fy_file = re.match(abstract_property_match_regex, fy_file_content)
        property_fy_file = re.match(property_match_regex, fy_file_content)

    if flow_fy_file:
        return ParsedFyFileKind.FLOW
    elif abstract_property_fy_file:
        return ParsedFyFileKind.ABSTRACT_PROPERTY
    elif property_fy_file:
        return ParsedFyFileKind.PROPERTY


def parse_flow_fy_file(file_path: Path) -> ParsedFyFile:
    flow_fy_regex = re.compile(
        r"flow (?P<flow_name>\w+):\n"
        r"\s+def -> (?P<return_type>[\w.]+):\n"
        r"(?P<flow_call_body>.*)",
        re.DOTALL
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        flow_fy_search = flow_fy_regex.search(fy_file_content)

    assert flow_fy_search is not None, f"File {file_path} is invalid flow fy file."

    parsed_fy_file = ParsedFlowFyFile(
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=FlowTemplateModel(
            flow_name=PythonEntityName.from_pascal_case(flow_fy_search.group("flow_name")),
            return_type=flow_fy_search.group("return_type"),
            flow_call_body=flow_fy_search.group("flow_call_body"),
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

    parsed_fy_file = ParsedAbstractPropertyFyFile(
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=AbstractPropertyTemplateModel(
            abstract_property_name=PythonEntityName.from_snake_case(
                abstract_property_fy_search.group("abstract_property_name")),
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

    parsed_fy_file = ParsedPropertyFyFile(
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=PropertyTemplateModel(
            property_name=PythonEntityName.from_snake_case(property_fy_search.group("property_name")),
            implementation_name=PythonEntityName.from_snake_case(property_fy_search.group("implementation_name")),
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
