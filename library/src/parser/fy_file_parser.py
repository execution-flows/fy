import re
from pathlib import Path

from domain.template_models import FlowTemplateModel, PropertyTemplateModel
from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileKind


def detect_fy_file_kind(file_path: Path) -> ParsedFyFileKind:
    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        flow_fy_file = re.match('flow', fy_file_content)
        property_fy_file = re.match('property', fy_file_content)

    if flow_fy_file:
        return ParsedFyFileKind.FLOW
    elif property_fy_file:
        return ParsedFyFileKind.ABSTRACT_PROPERTY


def parse_flow_fy_file(file_path: Path) -> ParsedFyFile:
    flow_fy_regex = re.compile(
        r"flow (?P<flow_name>\w+):\n"
        r"\s*def -> (?P<return_type>\w+):\n"
        r"(?P<flow_call_body>.*)",
        re.DOTALL
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        flow_fy_search = flow_fy_regex.search(fy_file_content)

    assert flow_fy_search is not None

    parsed_fy_file = ParsedFyFile(
        file_type=ParsedFyFileKind.FLOW,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=FlowTemplateModel(
            flow_name=flow_fy_search.group("flow_name"),
            return_type=flow_fy_search.group("return_type"),
            flow_call_body=flow_fy_search.group("flow_call_body"),
        )
    )

    return parsed_fy_file


def parse_abc_property_fy_file(file_path: Path) -> ParsedFyFile:
    property_fy_regex = re.compile(
        r"property (?P<property_name>\w+)"
        r" -> (?P<return_type>\w+)"
    )

    with file_path.open() as fy_file:
        fy_file_content = fy_file.read()
        property_fy_search = property_fy_regex.search(fy_file_content)

    assert property_fy_search is not None

    parsed_fy_file = ParsedFyFile(
        file_type=ParsedFyFileKind.ABSTRACT_PROPERTY,
        output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
        template_model=PropertyTemplateModel(
            property_name=property_fy_search.group("property_name"),
            return_type=property_fy_search.group("return_type"),
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
