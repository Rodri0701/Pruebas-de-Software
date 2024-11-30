from src.main2 import sum, sub, div
import pytest 

def test_sum():
    assert sum(1,2) == 3

def test_sub():
    assert sub(3,1) == 2

@pytest.mark.parametrize("x, y, expected", [
    (6, 3, 2),
    (10, 2, 5),
    (7, 2, 3.5),
    (0, 5, 0),
    (5, 1, 5)
])
def test_div(x, y, expected):
    assert div(x, y) == pytest.approx(expected) 