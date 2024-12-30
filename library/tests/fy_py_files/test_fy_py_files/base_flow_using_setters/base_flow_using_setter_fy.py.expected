"""fy
base flow SetterTest -> None:
    property greeting
    property greeting2
fy"""

import abc
from fy_core.base.flow_base import FlowBase
from fy_py_files.test_fy_py_files.base_flow_using_setters.greeting.abc_fy import (
    Greeting_PropertyMixin_ABC,
)
from fy_py_files.test_fy_py_files.base_flow_using_setters.greeting2.abc_fy import (
    Greeting2_PropertyMixin_ABC,
)


# fy:start ===>>>
class SetterTest_BaseFlow(
    # Abstract Property Mixins
    Greeting_PropertyMixin_ABC,
    Greeting2_PropertyMixin_ABC,
    # Base
    FlowBase[None],
    abc.ABC,
):
    pass
    # fy:end <<<===
