
import os
import requests
import json
from jsonpath_ng import jsonpath, parse, DatumInContext

class ClientConfig():
    def __init__(
        self,
        server: str = os.getenv("CONFIG_SERVER", "http://localhost:8888"),
        app_name: str = os.getenv("CONFIG_APPNAME"),
        profile: str = os.getenv("CONFIG_PROFILE"),
        label: str = os.getenv("CONFIG_LABEL")
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
        respone = requests.get(self.get_url())
        if respone.status_code == requests.codes.ok:
            self.json = respone.json()
            self.result = json.loads(self.json)
            return self.result
        else:
            return {}

    def get_properties(self) -> dict:
        return self.result["propertySources"]

    def get_property_rec(self, name):
        def get_val(v: dict, name: str):
            if type(v) == dict and v.get(name) is not None:
                return v.get(name)
            if type(v) == dict:
                for key in v:
                    if type(v.get(key)) == dict:
                        ret = get_val(v.get(key), name)
                        if ret is not None:
                            return ret
                        return get_val(v.get(key), name)
            return None

        sources = self.result["propertySources"]
        if type(sources) == list:
            for source in sources:
                if type(source) == dict and source.get('source') is not None:
                    v = source.get('source')
                    ret = get_val(v, name)
                    if ret is not None:
                        return ret
        return None

    def get_property(self, name) -> str:
        expression = f'$.propertySources[*].source.{name}'
        jsonpath = parse(expression)
        res: DatumInContext = jsonpath.find(self.result)

        # res2 = parse('propertySources[*].source').find(self.result)
        # res3 = json.loads(self.json).get('propertySources')
        #
        # jsonpath_expr = parse('foo[*].baz')
        # res4 = parse('foo[*].baz').find({'foo': [{'baz': 1}, {'baz': 2}]})
        # res5 = parse('$.name').find('{"name": "it" }')
        if len(res) > 0:
            return res[0].value
        return None
