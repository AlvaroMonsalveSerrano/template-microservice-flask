from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass(unsafe_hash=True)
class UseCaseRequest:
    uuid: str
    name: str
    operation: str
    operator: int


@dataclass(unsafe_hash=True)
class UseCaseResponse:
    resul: str


class UseCaseEntity:

    def __init__(self,
                 uuid: str,
                 name: str,
                 operation: str,
                 operator: int,
                 date_data: Optional[date] = None):
        self.uuid = uuid
        self.name = name
        self.operation = operation
        self.operator = operator
        self.date = date_data

    @property
    def calculate(self) -> int:
        result = 0
        if self.operation == "+":
            result = self.operator + self.operator
        elif self.operation == "*":
            result = self.operator * self.operator
        else:
            result = -1
        return result