import pytest

@pytest.fixture
def setUp():
    print("open amazon app")
    print("user logged in")
    yield
    print("logged out")
    print("closed amazon")


def test_addItemtoCart(setUp):
    print("added successfully")

def test_RemoveItemfromCart(setUp):
    print("removed suucessfully")


