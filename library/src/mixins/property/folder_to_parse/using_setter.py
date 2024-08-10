

class FolderToParse_PropertyMixin:
    @property
    def _folder_to_parse(self) -> str:
        return self.__folder_to_parse

    @_folder_to_parse.setter
    def _folder_to_parse(self, folder_to_parse: str) -> None:
        self.__folder_to_parse = folder_to_parse
