import pytest

@pytest.fixture
def setUp():
    print("setUp started")
    yield
    print("exited")


def test_addItemtoCart(setUp):
    print("added successfully")

def test_RemoveItemfromCart(setUp):
    print("removed suucessfully")


