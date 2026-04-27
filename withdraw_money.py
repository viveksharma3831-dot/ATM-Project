import utils


def withdraw_money():
    amount = input("Enter amount to withdraw: ")

    if not amount.isdigit():
        print("Please enter a valid number")
        return

    amount = int(amount)

    if amount > utils.balance:
        print("Insufficient balance")
    else:
        utils.balance = utils.balance - amount
        utils.statement.append("Withdrawn Rs " + str(amount))
        print("Money withdrawn successfully")
