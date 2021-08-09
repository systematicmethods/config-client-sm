
import os

class ClientConfig():
    def __init__(
        self,
        server = os.getenv("CONFIGSERVER", "http://localhost:8888"),
        app_name = os.getenv("APPNAME"),
        profile = os.getenv("PROFILE"),
        label = os.getenv("LABEL")
    ):
        self.server = server
        self.app_name = app_name
        self.profile = profile
        self.label = label

    def get_url(self) -> str:
        return f"{self.server}/{self.app_name}/{self.profile}/{self.label}"

