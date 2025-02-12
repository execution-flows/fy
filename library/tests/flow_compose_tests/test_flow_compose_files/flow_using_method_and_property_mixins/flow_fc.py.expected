from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(str, value="Hello world"),
    greet=greet__using_greeting,
)
def hello_world(
    greeting: FlowArgument[str],
    greet: FlowFunction[None],
) -> None:
    greet()
    print(greeting())
