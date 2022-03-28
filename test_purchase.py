import pytest

@pytest.fixture
def setUp():
    print("user logged in")
    yield
    print("logged out")


def test_addItemtoCart(setUp):
    print("added successfully")

def test_RemoveItemfromCart(setUp):
    print("removed suucessfully")


