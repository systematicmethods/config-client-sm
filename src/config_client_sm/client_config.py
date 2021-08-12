
import os
import requests
import json
from jsonpath_ng import jsonpath, parse

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
        self.result = dict()
        self.json = '{}'

    def get_url(self) -> str:
        return f"{self.server}/{self.app_name}/{self.profile}/{self.label}"

    def load(self) -> dict:
        self.json = requests.get(self.get_url()).json()
        self.result = json.loads(self.json)
        return self.result

    def get_properties(self) -> dict:
        return self.result["propertySources"]

    def get_property(self, name):
        sources = self.result["propertySources"]
        if type(sources) == list:
            for source in sources:
                if type(source) == dict and source.get('source') is not None:
                    v = source.get('source')
                    if type(v) == dict and v.get(name) is not None:
                        return v[name]

    def get_property3(self, name):
        expression = f'$.propertySources[*].{name}'
        jsonpath = parse(expression)
        res =  jsonpath.find(json)
        return res
