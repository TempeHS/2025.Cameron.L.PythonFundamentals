def main():
    while True:
        try:
            user = input("Enter a fraction: ")
            x, y = [int(number) for number in user.split("/")]
            output = round(x / y * 100)
            print(f"Your fuel percentage is: {output}%")
            if output <= 1:
                print("E")
                break
            elif 99 < output < 100:
                print("F")
                break
            elif output > 100:
                print("Invalid, output cannot be >100")
            else:
                break

        except ValueError:
            print("Invalid input, please enter valid numbers")

        except ZeroDivisionError:
            print("The denominator cannot be 0, please enter valid numbers")


main()
