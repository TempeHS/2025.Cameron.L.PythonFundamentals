total = 0


def coke(user):
    return int(user)


def main():
    total = 0
    user = input("How much would you like to enter in cents?")
    total += coke(user)
    while total <= 50:
        print("Amount Due:", 50 - total)
        user = input("How much would you like to enter in cents?")
        total += coke(user)
    if total >= 50:
        print("Change owed:", total - 50)


main()
