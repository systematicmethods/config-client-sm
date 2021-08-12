# import requests for the purposes of monkeypatching
import requests
import pytest
from mock_response import MockResponse


@pytest.fixture(scope="module")
def mock_response():
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""
    def mock_get(*args, **kwargs):
        return MockResponse({"mock_key": "mock_response"})
    setattr(requests, "get", mock_get)
