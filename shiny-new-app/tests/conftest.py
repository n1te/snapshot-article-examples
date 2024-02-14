import pytest
from fastapi.testclient import TestClient

from app import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(scope='module')
def vcr_config():
    return {'ignore_hosts': ['testserver']}
