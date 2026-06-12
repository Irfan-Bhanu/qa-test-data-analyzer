import pytest

from utils.data_reader import read_json_data
data=read_json_data("login_data.json")

@pytest.mark.parametrize(
    "user",
    data
)

def test_json(user):
    print(user["username"])
    print(user["password"])