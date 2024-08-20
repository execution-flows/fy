from pathlib import Path

from entry.main_flow import Main_Flow


def fy(
    folder_to_parse: Path,
    project_root_folder: Path,
) -> None:
    Main_Flow(
        folder_to_parse=Path(folder_to_parse),
        project_root_folder=(
            Path(project_root_folder) if project_root_folder is not None else Path.cwd()
        ),
    )()
