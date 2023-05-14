import pytest

@pytest.fixture()
def anyname():
    return "Devops Unv"

    yield
    print("Yield statement")
    
def test_sampletest(anyname):
    assert anyname == "Devops Unv"