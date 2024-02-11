def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print("Leave $%.2f" % tip)


def dollars_to_float(d):
    money = d.replace("$", "")  # Remove the $
    # Convert to float
    return float(money)


def percent_to_float(p):
    coin = p.replace("%", " ")
    # Convert to float and divide by 100 to get decimal representation
    return float(coin) / 100


main()
