
from config_client_sm import ClientConfig

def test_url():
    c = ClientConfig("http://localhost:8888", "myapp", "local,linux", "microservices")
    print(c.get_url())
    assert c.get_url() == "http://localhost:8888/myapp/local,linux/microservices"
