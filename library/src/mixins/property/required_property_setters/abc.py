import abc

from typing import List

from domain.parsed_fy_file import ParsedFyFile


class With_RequiredPropertySetters_PropertyMixin_ABC(abc.ABC):
    @property
    @abc.abstractmethod
    def _required_property_setters(self) -> List[ParsedFyFile]:
        raise NotImplementedError()
