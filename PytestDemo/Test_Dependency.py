import pytest

@pytest.mark.dependency()
def test_login():
    assert True

@pytest.mark.dependency(depends=["test_login"])
def test_search():
    assert True

@pytest.mark.dependency(depends=["test_search"])
def test_logout():
    assert True