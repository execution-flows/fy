from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(SpanishGreeting),
)
def hello_world2(
    greeting: FlowFunction[SpanishGreeting],
) -> str:
    return greeting()
