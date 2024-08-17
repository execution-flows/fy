from pathlib import Path


property folder_to_parse using setter:
    def -> Path:
        return self.__folder_to_parse

    @_folder_to_parse.setter
    def _folder_to_parse(self, folder_to_parse: Path) -> None:
        self.__folder_to_parse = folder_to_parse
