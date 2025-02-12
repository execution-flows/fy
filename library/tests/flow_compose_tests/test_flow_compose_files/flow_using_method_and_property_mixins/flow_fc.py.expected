from flow_compose import flow, FlowArgument, FlowFunction


@flow(
    greeting=FlowArgument(str, value="Hello world"),
    greet=greet__using_greeting,
)
def hello_world(
    greet: FlowFunction[None],
) -> None:
    greet()
