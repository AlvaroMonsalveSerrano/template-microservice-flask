import uuid
import logging

from datetime import date
from domain import entity_model


logging.basicConfig(level=logging.DEBUG)


def test_use_case_request():
    obj = entity_model.UseCaseRequest(uuid='{12345678-1234-5678-1234-567812345678}',
                                      name="name",
                                      operation="+",
                                      operator=10)
    assert obj is not None
    assert obj.uuid == '{12345678-1234-5678-1234-567812345678}'
    assert obj.name == "name"
    assert obj.operation == "+"
    assert obj.operator == 10


def test_use_case_response():
    obj = entity_model.UseCaseResponse(resul="ok")
    assert obj is not None
    assert obj.resul == "ok"


def test_use_case_entity_sum_with_date():
    obj = entity_model.UseCaseEntity(uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                                     name="name",
                                     operation="+",
                                     operator=10,
                                     date_data=date.today())
    assert obj is not None
    assert obj.calculate == 20


def test_use_case_entity_sum_without_date():
    obj = entity_model.UseCaseEntity(uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                                     name="name",
                                     operation="+",
                                     operator=10)
    assert obj is not None
    assert obj.calculate == 20


def test_use_case_entity_multiplication():
    obj = entity_model.UseCaseEntity(uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                                     name="name",
                                     operation="*",
                                     operator=10,
                                     date_data=date.today())
    assert obj is not None
    assert obj.calculate == 100


def test_use_case_entity_other():
    obj = entity_model.UseCaseEntity(uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                                     name="name",
                                     operation="/",
                                     operator=10,
                                     date_data=date.today())
    assert obj is not None
    assert obj.calculate == -1
