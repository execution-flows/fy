import abc
from typing import Generic, TypeVar

ResultT = TypeVar("ResultT")


class ExecutionFlowBase(Generic[ResultT], abc.ABC):
    @abc.abstractmethod
    def __call__(self) -> ResultT:
        raise NotImplementedError()
