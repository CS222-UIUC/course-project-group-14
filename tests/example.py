import pytest

@pytest.fixture
def example():
    return 200 + 22

def test_with_fixture(example):
    assert example == 222
