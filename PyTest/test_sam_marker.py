import pytest

@pytest.mark.regression
def test_Add():
    print("add method")


@pytest.mark.other
def test_Sub():
    print("Sub method")

@pytest.mark.sanity 
@pytest.mark.regression
def test_Mul():
    print("Mul method")