from services.make_change import MakeChange
from services.errors import NoChangeRequired, ValueTooSmallError

if __name__ == "__main__":
    """
    Start MakeChange Application.
    """
    make_change = MakeChange("15.00", "19.99")
    try:
        change, total_change = make_change.get_change()
        print(f"Total change owned: {total_change}")
        for coin in change.items():
            print(f"Denomination = {coin[0]} Number Returned = {coin[1]}")
    except ValueTooSmallError:
        print("Customer still owes more money...")
    except NoChangeRequired:
        print("No change needed exact change was provied by the customer.")
    