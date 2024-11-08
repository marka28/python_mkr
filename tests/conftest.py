import pytest


@pytest.fixture(scope='module')
def set_module():
    print("Start Test")
    yield
    print("\nFinish Test")