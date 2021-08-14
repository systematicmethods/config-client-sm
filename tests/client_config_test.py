import json

import requests
from config_client_sm import ClientConfig
from mock_response import MockResponse


def test_url_param():
    c = ClientConfig(server= 'http://localhost:8888',
                     app_name= 'myapp',
                     profile= 'local,linux',
                     label= 'microservices')
    assert c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'


def test_url():
    c = ClientConfig('http://localhost:8888',
                     'myapp',
                     'local,linux',
                     'microservices')
    assert c.get_url() == 'http://localhost:8888/myapp/local,linux/microservices'


def test_load(monkeypatch):
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


def test_prop(monkeypatch):
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


def test_prop_rec(monkeypatch):
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
    assert c.get_property_rec('foo') == 'myappsbar'
    assert c.get_property_rec('baz') == 'bam'
    assert c.get_property_rec('p1') == 'p11'
    assert c.get_property_rec('p3') == 'p31'
    assert c.get_property_rec('p31') is None


def test_prop_rec_flat(monkeypatch):
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
    assert c.get_property_rec('foo') == 'myappsbar'
    assert c.get_property_rec('baz') == 'bam'
    assert c.get_property_rec('foo1.p1') == 'p11'
    assert c.get_property_rec('foo1.foo1.p3') == 'p31'
    assert c.get_property_rec('p31') is None
