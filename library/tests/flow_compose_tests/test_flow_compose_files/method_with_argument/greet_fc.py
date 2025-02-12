from flow_compose import flow_function


@flow_function()
def greet__using_constant(greeting: str) -> int:
    print(greeting)
    return 1
