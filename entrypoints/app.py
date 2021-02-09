"""
To run application:

1.-
    >cd entrypoints/
    >export FLASK_APP=app.py
    >flask run

2.-
    >FLASK_APP=app.py flask run

To test application:

    >curl http://localhost:5000/
"""

import uuid
import logging

from flask import Flask, jsonify, request, current_app
from domain import entity_model
from repository import use_case_repository
from services import use_case_service

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=['GET'])
def root():
    """
    Root entrypoint
    :return: str
    """
    current_app.logger.info(f"[*] /root")
    return jsonify({'result': 'Ok'}), 200


@app.route("/liveness", methods=['GET'])
def liveness():
    """
    Liveness entrypoint.
    :return: str
    """
    current_app.logger.info(f"[*] /liveness")
    return 'Ok', 200


@app.route("/rediness", methods=['GET'])
def rediness():
    """
    Rediness entrypoint.
    :return: str
    """
    current_app.logger.info(f"[*] /rediness")
    return 'Ok', 200


@app.route("/use_case_example", methods=['POST'])
def do_use_case_example():
    """
    use case example

    curl --header "Content-Type: application/json" --request POST \
         --data '{"name":"xyz1", "operation":"+", "operator":"20"}' \
         http://localhost:5000/use_case_example

    :return: str
    """
    p_name = request.json['name']
    p_operation = request.json['operation']
    p_operator = int(request.json['operator'])
    current_app.logger.info(f"[*] /use_case_example")
    current_app.logger.info(f"[*] Request: Name={p_name} operation={p_operation} operator={p_operator}")

    current_app.logger.info(f"Name={p_name} operation={p_operation} operator={p_operator}")

    data_request = entity_model.UseCaseRequest(uuid=uuid.UUID,
                                               name=p_name,
                                               operation=p_operation,
                                               operator=p_operator)

    repository = use_case_repository.UseCaseRepository()
    response_use_case = use_case_service.do_something(data_request, repository)

    data = jsonify({'result': response_use_case.resul})

    return data, 200
