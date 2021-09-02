
import requests


# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:
    def __init__(self, jsondata):
        self.jsondata = jsondata
        self.status_code = requests.codes.ok

    # mock json() method always returns a specific testing dictionary
    # @staticmethod
    def json(self) -> dict[str, str]:
        # return {"mock_key": "mock_response"}
        return self.jsondata

