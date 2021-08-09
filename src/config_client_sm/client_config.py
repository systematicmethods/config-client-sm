
import os
import requests

class ClientConfig():
    def __init__(
        self,
        server: str = os.getenv("CONFIG_SERVER", "http://localhost:8888"),
        app_name: str  = os.getenv("CONFIG_APPNAME"),
        profile: str  = os.getenv("CONFIG_PROFILE"),
        label: str  = os.getenv("CONFIG_LABEL")
    ):
        self.server = server
        self.app_name = app_name
        self.profile = profile
        self.label = label

    def get_url(self) -> str:
        return f"{self.server}/{self.app_name}/{self.profile}/{self.label}"

    def load(self) -> dict:
        result = requests.get(self.get_url())
        return result.json()

