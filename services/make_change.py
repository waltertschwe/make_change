from decimal import Decimal, ROUND_DOWN
from dataclasses import dataclass
from typing import Tuple

from services.errors import NoChangeRequired, ValueTooSmallError


@dataclass
class MakeChange:
    """
    MakeChange class processes data input from the customer and
    helps to return the correct amount of change.
    """

    total_cost: str
    paid: str
    denominations = {
        "QUARTER": Decimal(".25"),
        "DIME": Decimal(".10"),
        "NICKEL": Decimal(".05"),
        "PENNY": Decimal(".01"),
    }

    def get_change(self) -> Tuple[dict, Decimal]:
        """
        Main entry point into the application to generate change.
        """
        results = {}
        cost_decimal, paid_decimal = self.clean_string_input_to_decimal()
        total_change = paid_decimal - cost_decimal
        if total_change.is_zero():
            raise NoChangeRequired

        if total_change < 0:
            raise ValueTooSmallError

        if total_change >= 1:
            results["DOLLARS"] = self.get_num_denomination_returned(total_change)
        else:
            results["DOLLARS"] = 0

        change_due = total_change - results["DOLLARS"]
        self.get_change_returned(change_due, results)

        return results, total_change

    def get_change_returned(self, change, results) -> dict:
        """
        Generic function to process USD change denominations.
        """
        for denomination in self.denominations.items():
            change_due = change / denomination[1]
            if change_due >= 1:
                results[denomination[0]] = self.get_num_denomination_returned(
                    change_due
                )
            else:
                results[denomination[0]] = 0

            change = change - (results[denomination[0]] * denomination[1])

        return results

    def get_num_denomination_returned(self, change) -> int:
        """
        Get the whole integer amount of the USD denomination to be returned
        to the customer.
        """
        return int(change.quantize(Decimal("1."), rounding=ROUND_DOWN))

    def clean_string_input_to_decimal(self) -> Tuple[Decimal, Decimal]:
        """
        Convert string input to Decimal format.
        """
        total_cost_num = Decimal(self.total_cost)
        paid_num = Decimal(self.paid)
        return (total_cost_num, paid_num)
