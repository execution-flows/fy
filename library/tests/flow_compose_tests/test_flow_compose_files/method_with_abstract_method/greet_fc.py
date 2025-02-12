from flow_compose import flow_function, FlowFunction


@flow_function()
def greet__using_constant(
    greeting_text: str,
    greeting: FlowFunction[str],
) -> int:
    print(greeting_text)
    return 1
