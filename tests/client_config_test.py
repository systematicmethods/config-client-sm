
from config_client_sm import ClientConfig

def test_url_param():
    c = ClientConfig(server= "http://localhost:8888",
                     app_name= "myapp",
                     profile= "local,linux",
                     label= "microservices")
    assert c.get_url() == "http://localhost:8888/myapp/local,linux/microservices"

def test_url():
    c = ClientConfig("http://localhost:8888",
                     "myapp",
                     "local,linux",
                     "microservices")
    assert c.get_url() == "http://localhost:8888/myapp/local,linux/microservices"
