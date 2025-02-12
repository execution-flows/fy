from flow_compose import flow_function


@flow_function()
def greet__using_greeting(message: str) -> str:
    return message
