
import uuid
import pytest
import logging

from domain import entity_model
from services import use_case_service
from exceptions import use_case_exception
from repository import use_case_repository


class FakeUseCaseRepository(use_case_repository.AbstractUseCaseRepository):
    """
    FakeUseCaseRepository to test.

    """

    def __init__(self) -> None:
        super().__init__()

    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        return True

    def get(self, uuid: str) -> entity_model.UseCaseEntity:
        return entity_model.UseCaseEntity(
                        uuid=uuid.UUID('{12345678-1234-5678-1234-567812345678}'),
                        name="name",
                        operation="+",
                        operator=10,
                        date_data=None)


logging.basicConfig(level=logging.DEBUG)


def test_do_something():
    id = uuid.UUID('{12345678-1234-5678-1234-567812345678}')
    request = entity_model.UseCaseRequest(uuid=id,
                                          name="name",
                                          operation="+",
                                          operator=10)
    repository = FakeUseCaseRepository()
    result = use_case_service.do_something(request, repository)
    assert result.resul == '20'


def test_do_something_request_is_none():
    with pytest.raises(use_case_exception.UseCaseRequestException):
        repository = FakeUseCaseRepository()
        use_case_service.do_something(None, repository)
