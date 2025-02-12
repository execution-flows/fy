from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(str),
)
def hello_world2(
    greeting: FlowFunction[str],
) -> str:
    return greeting()
