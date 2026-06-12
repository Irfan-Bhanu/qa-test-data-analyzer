from pages.login_page import  LoginPage

def test_basic_auth(login_page,test_data):


    login_page.open_basic_auth_direct(test_data["username"],
                                      test_data["password"])

    assert "Congratulations! You must have the proper credentials" in login_page.driver.page_source

