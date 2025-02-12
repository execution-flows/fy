from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(SpanishGreeting, value="Hola Mundo!"),
)
def hello_world(
    greeting: FlowFunction[SpanishGreeting],
) -> None:
    print(greeting())
