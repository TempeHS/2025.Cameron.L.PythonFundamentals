def main():
    math = input("What is the equation?")
    x, y, z = math.split(" ")

    match math:
        case "x + y":
            print(x, y, z)
        case "x - y":
            print(x - z)
        case "x/y":
            print(x / y)
        case "x * y":
            print(x * y)


main()
