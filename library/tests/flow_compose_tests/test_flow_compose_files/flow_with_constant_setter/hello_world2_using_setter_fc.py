from flow_compose import flow, FlowArgument


@flow(
    greeting=FlowArgument(str),
)
def hello_world2(
    greeting: FlowArgument[str],
) -> str:
    return greeting()
