import pytest
from hello import suma

def test_suma():
    assert suma(3, 5) == 8
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(1.5, 2.5) == 4.0
    assert suma(-1.5, -2.5) == -4.0

def test_suma_float():
    assert suma(1.1, 2.2) == 3.3
    assert suma(-1.1, -2.2) == -3.3
    assert suma(1.1, -2.2) == -1.1
    assert suma(-1.1, 2.2) == 1.1
