from flow_compose import flow, FlowArgument


@flow(
    greeting=FlowArgument(str, value="Hello World"),
)
def hello_world(
    greeting: FlowArgument[str],
) -> str:
    return greeting()
