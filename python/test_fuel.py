import pytest
from fuel import convert, gauge


def test_convert():
    # Test valid inputs
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1

    # Test edge cases
    with pytest.raises(ValueError):
        convert("2/1")  # X > Y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Y == 0
    with pytest.raises(ValueError):
        convert("a/b")  # Non-integer values
    with pytest.raises(ValueError):
        convert("3.5/4")  # Float values


def test_gauge():
    # Test percentages
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
