import decimal
from services.make_change import MakeChange
from services.errors import NoChangeRequired, ValueTooSmallError

if __name__ == "__main__":
    """
    Start MakeChange Application.
    """

   
    total_cost = input("Enter Total Cost: ")
    paid = input("Enter Amount Provided: ")
    
    make_change = MakeChange(total_cost, paid)
    try:
        change, total_change = make_change.get_change()
        print(f"Total change owned: {total_change}")
        for coin in change.items():
            print(f"Denomination = {coin[0]} Number Returned = {coin[1]}")
    except decimal.InvalidOperation:
        print("Bad input data.  Please try again.")
    except ValueTooSmallError:
        print("Customer still owes more money...")
    except NoChangeRequired:
        print("No change needed exact change was provied by the customer.")
