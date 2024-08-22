import abc

from typing import Dict

from domain.parsed_fy_py_file import ParsedFyPyFile


class With_ParseFyPyFilesMapByKey_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _parse_fy_py_files_map_by_key(self) -> Dict[str, ParsedFyPyFile]:
        raise NotImplementedError()
