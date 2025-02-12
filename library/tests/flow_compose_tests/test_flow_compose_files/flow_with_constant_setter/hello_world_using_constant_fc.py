from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(str, value="Hello World"),
)
def hello_world(
    greeting: FlowFunction[str],
) -> str:
    return greeting()
