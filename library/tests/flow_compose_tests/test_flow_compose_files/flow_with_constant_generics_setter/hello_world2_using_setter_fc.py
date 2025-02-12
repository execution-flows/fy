from flow_compose import flow, FlowArgument


@flow(
    greeting=FlowArgument(SpanishGreeting),
)
def hello_world2(
    greeting: FlowArgument[SpanishGreeting],
) -> str:
    return greeting()
