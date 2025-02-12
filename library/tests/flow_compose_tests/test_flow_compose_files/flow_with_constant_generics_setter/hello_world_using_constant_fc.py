from flow_compose import flow, FlowArgument


@flow(
    greeting=FlowArgument(SpanishGreeting, value="Hola Mundo!"),
)
def hello_world(
    greeting: FlowArgument[SpanishGreeting],
) -> None:
    print(greeting())
