from services.make_change import MakeChange
from services.errors import NoChangeRequired, ValueTooSmallError

if __name__ == "__main__":
    """
    Start MakeChange Application.
    """
    amount_owed = "15.00"
    customer_paid = "19.99"

    make_change = MakeChange(amount_owed, customer_paid)
    try:
        change, total_change = make_change.get_change()
        print(f"Total change owned: {total_change}")
        for coin in change.items():
            print(f"Denomination = {coin[0]} Number Returned = {coin[1]}")
    except ValueTooSmallError:
        print("Customer still owes more money...")
    except NoChangeRequired:
        print("No change needed exact change was provied by the customer.")
    