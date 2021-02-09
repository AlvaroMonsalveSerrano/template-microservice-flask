
import uuid

from datetime import date
from repository import use_case_repository
from domain import entity_model


def create_uuid_to_test() -> uuid.UUID:
    return uuid.UUID('{12345678-1234-5678-1234-567812345678}')


def create_entity_to_test() -> entity_model.UseCaseEntity:
    return entity_model.UseCaseEntity(uuid=create_uuid_to_test(),
                                      name="name",
                                      operation="+",
                                      operator=10,
                                      date_data=date.today())


def test_create_repository():
    repository = use_case_repository.UseCaseRepository()
    assert repository is not None


def test_add_entity_use_case():
    repository = use_case_repository.UseCaseRepository()

    entity = create_entity_to_test()

    result: bool = repository.add(entity)
    assert result is not None
    assert result is True


def test_get_entity():
    repository = use_case_repository.UseCaseRepository()
    entity = create_entity_to_test()
    result: bool = repository.add(entity)
    assert result is not None
    assert result is True

    result_entity = repository.get(str(create_uuid_to_test()))
    assert result_entity is not None
    assert result_entity == entity
    # assert result_entity.uuid == entity.uuid
