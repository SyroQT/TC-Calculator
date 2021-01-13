import pytest

from src.calculator import Calculator


def test_init():
    cal = Calculator()
    assert str(cal) == "0"


def test_state_getter():
    cal = Calculator(6)
    assert cal.state == 6


def test_add():
    cal = Calculator(1)
    cal.add(3)
    assert  cal.state == 4


def test_sub():
    cal = Calculator(3)
    cal.sub(1)
    assert  cal.state == 2


def test_mult():
    cal = Calculator(2)
    cal.mult(3)
    assert cal.state == 6


def test_div():
    cal = Calculator(8)
    cal.div(2)
    assert cal.state == 4


def test_root():
    cal = Calculator(9)
    cal.root()
    assert cal.state == 3


def test_reset():
    cal = Calculator(42)
    cal.reset()
    assert cal.state == 0


def test_div_zero():
    cal = Calculator(66)
    with pytest.raises(ZeroDivisionError):
        cal.div(0)


def test_str_input():
    with pytest.raises(ValueError):
        cal = Calculator("test")
