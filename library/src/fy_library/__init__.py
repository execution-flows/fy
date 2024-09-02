# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

# This is the exported file from the library when installed as a package in other projects. Whatever is imported in
# this file is accessible in projects that install `fy_library` package. Currently, CLI tool uses `Main_Flow` to run
# the tool.

from fy_library.fy import fy

__all__ = ["fy"]
