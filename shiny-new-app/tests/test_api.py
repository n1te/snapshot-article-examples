import pytest


@pytest.mark.vcr
def test_favorite_beer_endpoint(client, snapshot):
    response = client.get('/api/beers/favorite')
    assert response.status_code == snapshot
    assert response.json() == snapshot
