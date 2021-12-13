import decimal
import pytest

from services.make_change import MakeChange
from services.errors import NoChangeRequired, ValueTooSmallError



def test_bad_input_data():
    """
    Test that we raise an error when we have bad Decimal data input.
    """
    with pytest.raises(decimal.InvalidOperation):
        make_change = MakeChange("bad_data", "needs_to_be_float")
        change, total_change = make_change.get_change()

def test_no_change_required():
    """
    Test that when the customer provides exact change we raise a
    NoChangeRequired exception.
    """
    with pytest.raises(NoChangeRequired):
        make_change = MakeChange("5.00", "5.00")
        change, total_change = make_change.get_change()


def test_not_enough_usd():
    """
    Test that when the customer provides not enough USD then we raise a
    ValueTooSmallError
    """
    with pytest.raises(ValueTooSmallError):
        make_change = MakeChange("7.00", "5.00")
        change, total_change = make_change.get_change()


def test_only_dollars():
    """
    Test that a customer provides change where only USD dollars and no
    coins are returned
    """
    make_change = MakeChange("5.00", "7.00")
    change, total_change = make_change.get_change()

    assert change == {
        "DOLLARS": 2,
        "QUARTER": 0,
        "DIME": 0,
        "NICKEL": 0,
        "PENNY": 0,
    }


@pytest.mark.parametrize(
    "total_cost,paid,expected",
    [
        (
            "5.25",
            "6.00",
            {
                "DOLLARS": 0,
                "QUARTER": 3,
                "DIME": 0,
                "NICKEL": 0,
                "PENNY": 0,
            },
        ),
        (
            "5.00",
            "5.99",
            {
                "DOLLARS": 0,
                "QUARTER": 3,
                "DIME": 2,
                "NICKEL": 0,
                "PENNY": 4,
            },
        ),
        (
            "14.90",
            "15.00",
            {
                "DOLLARS": 0,
                "QUARTER": 0,
                "DIME": 1,
                "NICKEL": 0,
                "PENNY": 0,
            },
        ),
        (
            ".90",
            ".99",
            {
                "DOLLARS": 0,
                "QUARTER": 0,
                "DIME": 0,
                "NICKEL": 1,
                "PENNY": 4,
            },
        ),
        (
            "20.00",
            "22.97",
            {
                "DOLLARS": 2,
                "QUARTER": 3,
                "DIME": 2,
                "NICKEL": 0,
                "PENNY": 2,
            },
        ),
        (
            "20.00",
            "21.49",
            {
                "DOLLARS": 1,
                "QUARTER": 1,
                "DIME": 2,
                "NICKEL": 0,
                "PENNY": 4,
            },
        ),
    ],
)
def test_various_change_combinations(total_cost, paid, expected):
    """
    Test Various Change Combinations
    """
    make_change = MakeChange(total_cost, paid)
    change, total_change = make_change.get_change()
    assert change == expected
