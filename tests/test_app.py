
import pytest

from app import add_numbers, divide_numbers


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-2, 3, 1),
        (0, 5, 5),
        (2.5, 1.5, 4.0),
        (2, 1.5, 3.5),
    ],
)
def test_add_numbers_valid_inputs(a, b, expected):
    assert add_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        ("2", 3),
        (2, "3"),
        (None, 3),
        (2, None),
        (True, 3),
        (2, False),
    ],
)
def test_add_numbers_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        add_numbers(a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5.0),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
        (0, 5, 0.0),
        (5, 2, 2.5),
        (5, 2.0, 2.5),
    ],
)
def test_divide_numbers_valid_inputs(a, b, expected):
    assert divide_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a, b",
    [
        ("10", 2),
        (10, "2"),
        (None, 2),
        (10, None),
        (True, 2),
        (10, False),
    ],
)
def test_divide_numbers_invalid_inputs(a, b):
    with pytest.raises(TypeError):
        divide_numbers(a, b)


@pytest.mark.parametrize("a", [1, -1, 0, 2.5])
def test_divide_numbers_by_zero(a):
    with pytest.raises(ZeroDivisionError):
        divide_numbers(a, 0)
