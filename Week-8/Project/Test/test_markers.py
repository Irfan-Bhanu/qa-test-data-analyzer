import pytest

@pytest.mark.login
def test_login(driver):
    pass

@pytest.mark.windows
def test_windows(driver):
    pass


@pytest.mark.action
def test_hover(driver):
    pass


@pytest.mark.action
def test_double_click(driver):
    pass


#run only login- pytest -m login
#run only window tests - pytest -m windows
#run only actionschain tests - pytest -m action
#exclude action test - pytest -m "not action"
#Multiple markers - pytest -m "login or windows"
