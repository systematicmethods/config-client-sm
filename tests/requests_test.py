

# our app.py that includes the get_json() function
# this is the previous code block example
from config_client_sm import requests_json as app


def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
