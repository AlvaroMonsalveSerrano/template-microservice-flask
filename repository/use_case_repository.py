import abc
import uuid

from domain import entity_model
from flask import current_app


class AbstractUseCaseRepository(abc.ABC):
    """
    Abstract class with the common operations of the entity UseCaseEntity
    """

    @abc.abstractmethod
    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> entity_model.UseCaseEntity:
        raise NotImplementedError


class UseCaseRepository(AbstractUseCaseRepository):
    """
    Definition of the operations that connect to a database.
    """

    def __init__(self) -> None:
        self.database: [entity_model.UseCaseEntity] = []

    def add(self, entity: entity_model.UseCaseEntity) -> bool:
        result: bool = False
        current_app.logger.info(f"[***] /use_case_repository.add")
        if entity is not None:
            result = True
            self.database.append(entity)
        return result

    def get(self, p_uuid: str) -> entity_model.UseCaseEntity:
        index = 0
        enc = False
        result: entity_model.UseCaseEntity = None
        current_app.logger.info(f"[***] /use_case_repository.get")
        while (index < len(self.database)) and not enc:
            aux: entity_model.UseCaseEntity = self.database[index]
            if aux.uuid == uuid.UUID(p_uuid):
                result = aux
                enc = True
            index += 1
        return result
