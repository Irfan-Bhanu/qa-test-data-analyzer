import pytest
from utils.data_reader import read_excel_data


data = read_excel_data(
    "login_data.xlsx"
)


@pytest.mark.parametrize(
    "username,password",
    data
)
def test_excel(
        username,
        password):

    print(username)
    print(password)