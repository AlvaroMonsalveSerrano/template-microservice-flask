"""
End to End test.

To run local aplication:

"""


import config
import pytest
import requests


# @pytest.mark.usefixtures('restart_api')
# def test_root():
#     url = config.get_api_url()
#     data = {}
#     # response = requests.get(f'{url}/', json=data)
#     response = requests.get(f'{url}/')
#
#     assert response.status_code == 201
#     assert response.json()['result'] == 'Ok'
