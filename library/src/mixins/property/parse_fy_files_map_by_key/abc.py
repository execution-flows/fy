import abc

from typing import Dict

from domain.parsed_fy_file import ParsedFyFile


class With_ParseFyFilesMapByKey_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parse_fy_files_map_by_key(self) -> Dict[str, ParsedFyFile]:
        raise NotImplementedError()
