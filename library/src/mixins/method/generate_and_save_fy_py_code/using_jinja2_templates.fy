method generate_and_save_fy_py_files using jinja2_templates:
    with property parsed_fy_py_files
    with property required_property_setters_fy_py
    with property mixin_import_map

    def -> None:
        print(self._parsed_fy_py_files)
        print(self._required_property_setters_fy_py)
        print(self._mixin_import_map)
