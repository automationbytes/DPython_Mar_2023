import pytest

def test_add():
    num1 = 10
    num2 = 15
    assert num1+num2 == 25


@pytest.mark.skip("Simply skip")
def testmul():
    num1 = 10
    num2 = 15
    print("Multiplication of the number",num1*num2)
    assert num1*num2 == 150

