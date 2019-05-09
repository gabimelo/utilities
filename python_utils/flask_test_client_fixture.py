import pytest


@pytest.fixture(scope='module')
def test_client():
    from src.server import app
    app.testing = True
    yield app.test_client()
