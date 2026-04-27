import utils


def deposit_money():
    amount = input("Enter amount to deposit: ")

    if not amount.isdigit():
        print("Please enter a valid number")
        return

    amount = int(amount)
    utils.balance = utils.balance + amount
    utils.statement.append("Deposited Rs " + str(amount))
    print("Money deposited successfully")
