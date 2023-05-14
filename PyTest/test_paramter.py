import pytest


@pytest.mark.parametrize("a,b,sum",[(1,2,3),(3,3,6),(2,2,5)])
def test_add(a,b,sum):
    assert sum == a+b