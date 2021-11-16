import pytest


@pytest.fixture(scope="function")
def test_log():
    return [
        "haskdj123 [DOCS] commit message 1",
        "10983nnfp [DOCS, PARSERS] commit message 2",
        "nck0a9123 [TOOLS, VBA] commit message 3",
    ]
