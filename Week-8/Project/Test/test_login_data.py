import pytest

@pytest.mark.parametrize(
    "username, password",
     [
         ("test","test123"),
         ("admin", "admin123"),
         ("user","wrongpassword")
     ]
     )
def test_login_data(username,password):
    print(username)
    print(password)