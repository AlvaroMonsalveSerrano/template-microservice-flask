"""
End to End test.

To run local aplication:

"""
import requests
import config


def test_root():
    url = config.get_api_url()
    data = {}
    response = requests.get(f'{url}/', json=data)
    print(f"1===>{response}")
    print(f"2===>{response.json()['result']}")

    assert response.status_code == 201
    assert response.json()['result'] == 'Ok'
