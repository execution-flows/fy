from flow_compose import flow_function, FlowFunction


@flow_function(cached=True)
def hello_world__using_spanish_greeting(
    greeting: FlowFunction[SpanishGreeting],
) -> str:
    return f"Hello World - {greeting()}"
