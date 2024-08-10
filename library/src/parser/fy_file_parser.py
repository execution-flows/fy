import re
from pathlib import Path

from domain.flow_template_model import FlowTemplateModel
from domain.parsed_fy_file import ParsedFyFile, ParsedFyFileType


class FyFileParser:
    @staticmethod
    def parse(file_path: Path) -> ParsedFyFile:
        flow_fy_regex = re.compile(
            r"flow (?P<flow_name>\w+):\n"
            r"(?P<flow_body>.*)",
            re.DOTALL
        )
        with file_path.open() as fy_file:
            fy_file_content = fy_file.read()
            flow_fy_search = flow_fy_regex.search(fy_file_content)

        assert flow_fy_search is not None

        parsed_fy_file = ParsedFyFile(
            file_type=ParsedFyFileType.FLOW,
            output_py_file_path=file_path.with_name(f"{file_path.stem}.py"),
            template_model=FlowTemplateModel(
                flow_name=flow_fy_search.group("flow_name"),
                flow_body=flow_fy_search.group("flow_body"),
            )
        )
        return parsed_fy_file