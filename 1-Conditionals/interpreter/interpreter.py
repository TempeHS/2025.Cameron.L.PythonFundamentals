def main():
    expression = input("Enter the equation")
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    if y == ("+"):
        print(x + z)
    elif y == ("-"):
        print(x - z)
    elif y == ("/"):
        print(x / z)
    elif y == ("*"):
        print(x * z)
    else:
        print("Invalid operator")


main()
