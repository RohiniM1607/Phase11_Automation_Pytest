import pytest_check as check

def test_sample():

    check.equal(10, 20)

    check.is_true(False)

    check.not_equal(5, 10)

    print("Execution continues even after failures")