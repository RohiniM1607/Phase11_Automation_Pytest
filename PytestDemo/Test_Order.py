import pytest 
@pytest.mark.order(3)
def test_sample_one():
    print("Hai")
@pytest.mark.order(1)
def test_sample1():
    print("Welcome")
@pytest.mark.order(2)
def test_sample2():
    print("Pytest")