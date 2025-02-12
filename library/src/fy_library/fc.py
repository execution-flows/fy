from pathlib import Path

from fy_library.flows.flow_compose_main_fy import FlowCompose_Main_Flow


def fc(
    folder_to_parse: Path,
    project_root_folder: Path,
    folder_to_generate: Path,
) -> None:
    FlowCompose_Main_Flow(
        folder_to_generate=folder_to_generate,
        folder_to_parse=folder_to_parse,
        project_root_folder=(
            Path(project_root_folder) if project_root_folder is not None else Path.cwd()
        ),
    )()
