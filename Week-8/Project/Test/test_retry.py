import pytest

@pytest.mark.flaky(reruns=2)
def test_retry():

    assert False