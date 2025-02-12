from flow_compose import flow_function, FlowFunction


@flow_function(cached=True)
def greet__using_constant(
    greeting: FlowFunction[str],
) -> int:
    print(greeting())
    print(greeting())
    return 1
