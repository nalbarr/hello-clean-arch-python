from calc.calc import Calc
import pytest

def test_add_two_numbers():
    c = Calc()
    res = c.add(4, 5)
    assert res == 9

def test_add_three_numbers():
    c = Calc()
    res = c.add(4, 5, 6)
    assert res == 15

def test_many_numbers():
    s = range(100)
    assert Calc().add(*s) == 4950

def test_subract_two_numbers():
    c = Calc()
    res = c.sub(10, 3)
    assert res == 7

def test_mul_two_numbers():
    c = Calc()
    res = c.mul(6, 4)
    assert res == 24

def test_mul_many_numbers():
    s = range(1, 10)
    assert Calc().mul(*s) == 362880

def test_mult_by_zero_raises_exception():
    c = Calc()
    with pytest.raises(ValueError):
        c.mul(3, 0)

def test_div_two_numbers_float():
    c = Calc()
    res = c.div(13, 2)
    assert (res == 6.5)

def test_div_by_zero_returns_inf():
    c = Calc()
    res = c.div(5, 0)
    assert res == "inf"

def test_avg_correct_average():
    "The function accepts an iterable and computes the average, i.e. avg([2, 5, 12, 98]) == 29.25"
    c = Calc()
    res = c.avg([2, 5, 12, 98])
    assert res == 29.25

def test_avg_remove_upper_outliers():
    "The function accepts an optional upper threshold. It must remove all the values that are greater than the threshold before computing the average, i.e. avg([2, 5, 12, 98], ut=90) == avg([2, 5, 12])"
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=90)
    assert res == pytest.approx(6.333333)

def test_avg_remove_lower_outliers():
    "The function accepts an optional lower threshold. It must remove all the values that are less then the threshold before computing the average, i.e. avg([2, 5, 12, 98], lt=10) == avg([12, 98])"
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=10)
    assert res == pytest.approx(55)

def test_avg_upper_threshold_is_included():
    "The upper threshold is not included in the comparison, i.e. avg([2, 5, 12, 98], ut=98) == avg([2, 5, 12, 98])"
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=98)
    assert res == pytest.approx(29.25)


def test_avg_lower_threshold_is_included():
    "The lower threshold is not included in the comparison, i.e. avg([2, 5, 12, 98], lt=5) == avg([5, 12, 98])"
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=2)
    assert res == pytest.approx(29.25)
