from config_client_sm import helpers

def func1(x):
    return x + 1

def test_answer():
    assert func1(3) == 4

def test_answer2():
    assert helpers.func(3) == 4


