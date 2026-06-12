import pytest

from utils.data_reader import read_csv_data

data= read_csv_data("login_data.csv")

@pytest.mark.parametrize(
    "username,password",
    data
)

def test_csv(username, password):
    print(username)
    print(password)