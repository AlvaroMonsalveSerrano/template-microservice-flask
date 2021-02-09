
import logging

from datetime import date
from domain import entity_model
from exceptions import use_case_exception
from repository import use_case_repository


def do_something(request: entity_model.UseCaseRequest,
                 repository: use_case_repository.AbstractUseCaseRepository) -> entity_model.UseCaseResponse:
    """
    Business operation.

    :param request: entity_model.UseCaseRequest
    :param repository: use_case_repository.AbstractUseCaseRepository

    :return: entity_model.UseCaseResponse
    """

    if request is None:
        raise use_case_exception.UseCaseRequestException()

    logging.info(f"[**] /use_case_service.do_something")

    entity = entity_model.UseCaseEntity(uuid=request.uuid,
                                        name=request.name,
                                        operation=request.operation,
                                        operator=request.operator,
                                        date_data=date.today())

    repository.add(entity)

    return entity_model.UseCaseResponse(str(entity.calculate))
