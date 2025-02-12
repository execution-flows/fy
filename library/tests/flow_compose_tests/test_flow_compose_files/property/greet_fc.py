from flow_compose import flow_function


@flow_function(cached=True)
def greet__using_constant() -> int:
    return 1
