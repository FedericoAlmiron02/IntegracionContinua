import pytest
from hello import suma

def test_suma():
    assert suma(3, 5) == 8
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(1.5, 2.5) == 4.0
    assert suma(-1.5, -2.5) == -4.0


