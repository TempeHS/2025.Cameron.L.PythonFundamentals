def main():
    grocery = {}
    while True:
        try:
            item = input("What is in your grocery list? ").upper().strip()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            break

    for a, b in grocery.items():
        print(f"{a}, {b}")


main()
