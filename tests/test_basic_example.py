import pytest


# Define a simple fixture
@pytest.fixture
def simple_data():
    return 42


# Test simple fixture
def test_simple_data(simple_data):
    assert simple_data == 42


Define a fixture with parameters
@pytest.fixture(params=[0, 1, 2])
def param_data(request):
    return request.param


# Test parametrized fixture
def test_param_data(param_data):
    assert param_data in [0, 1, 2]


Define a fixture that takes an argument
@pytest.fixture
def square(request):
    return request.param * 2


# Use indirect parametrization to pass arguments to the fixture
@pytest.mark.parametrize("square", [1, 2, 3], indirect=True)
def test_square(square):
    assert square in [2, 4, 6]


# Use Factories as fixture
@pytest.fixture
def user_creds():
    def _user_creds(name: str, email: str):
        return {"name": name, "email": email}

    return _user_creds


def test_user_creds(user_creds):
    assert user_creds("John", "abc@xyz.com") == {
        "name": "John",
        "email": "abc@xyz.com",
    }
