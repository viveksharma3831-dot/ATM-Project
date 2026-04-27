from utils import statement


def show_statement():
    print("\nMini Statement")
    if len(statement) == 0:
        print("No transaction found")
    else:
        for item in statement:
            print(item)
