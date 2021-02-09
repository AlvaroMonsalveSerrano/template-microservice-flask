
import pytest


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
def test_liveness(app, client):
    res = client.get('/liveness')
    assert res.status_code == 200


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('client')
def test_rediness(app, client):
    response = client.get('/rediness')
    assert response.status_code == 200