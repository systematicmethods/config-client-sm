import json

import requests
from config_client_sm import ClientConfig
from mock_response import MockResponse


def test_should_have_url_by_named_param():
    c = ClientConfig(server= 'http://localhost:8888',
                     app_name= 'myapp',
                     profile= 'local,linux',
                     label= 'microservices')
    assert c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'


def test_should_have_url():
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    assert c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'


def test_load_int_dict(monkeypatch):
    with open('spring_cloud_config.json', 'r') as file:
        data = file.read().replace('\n', '')

    def mock_get(*args, **kwargs):
        return MockResponse(data)

    monkeypatch.setattr(requests, 'get', mock_get)
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'
    j = c.load()
    assert j is not None
    assert j == json.loads(data)


def test_get_property_by_name_v1(monkeypatch):
    with open('spring_cloud_config.json', 'r') as file:
        data = file.read().replace('\n', '')

    def mock_get(*args, **kwargs):
        return MockResponse(data)

    monkeypatch.setattr(requests, 'get', mock_get)
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'
    j = c.load()
    assert j is not None
    assert c.get_properties() == json.loads(data)['propertySources']
    assert c.get_property('baz') == 'bam'


def test_get_property_by_nested_name(monkeypatch):
    with open('spring_cloud_config.json', 'r') as file:
        data = file.read().replace('\n', '')

    def mock_get(*args, **kwargs):
        return MockResponse(data)

    monkeypatch.setattr(requests, 'get', mock_get)
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'
    j = c.load()
    assert j is not None
    assert c.get_property('foo') == 'myappsbar'
    assert c.get_property('p1') == 'p11'
    assert c.get_property('p3') == 'p31'
    assert c.get_property('p31') is None


def test_get_property_by_name_flat(monkeypatch):
    with open('spring_cloud_config.json', 'r') as file:
        data = file.read().replace('\n', '')

    def mock_get(*args, **kwargs):
        return MockResponse(data)

    monkeypatch.setattr(requests, 'get', mock_get)
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'
    j = c.load()
    assert j is not None
    assert c.get_property('foo') == 'myappsbar'
    assert c.get_property('baz') == 'bam'
    assert c.get_property('foo1.p1') == 'p111'
    assert c.get_property('foo1.foo2.p1') == 'p1211'
    assert c.get_property('p31') is None


def test_get_property_by_name_substituted(monkeypatch):
    with open('spring_cloud_config.json', 'r') as file:
        data = file.read().replace('\n', '')

    def mock_get(*args, **kwargs):
        return MockResponse(data)

    monkeypatch.setattr(requests, 'get', mock_get)
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'
    j = c.load()
    assert j is not None
    assert c.get_property('foo') == 'myappsbar'
    assert c.get_property('foo1.foo2.p3') == 'server_int_1'
