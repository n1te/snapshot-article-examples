import pytest
from app import app


@pytest.fixture
def client():
    app.config.update({
        'TESTING': True,
    })

    with app.test_client() as client:
        with app.app_context():
            yield client
