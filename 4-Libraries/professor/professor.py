import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            print("Please enter a valid level (1, 2, or 3).")
        except ValueError:
            print("Please enter a valid integer.")


def generate_integer(level):
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    return x, y


def main():
    correct = 0
    attempts = 0

    level = get_level()

    for _ in range(10):
        x, y = generate_integer(level)
        answer = x + y

        for _ in range(3):
            try:
                user_answer = int(input(f"What's the answer to {x} + {y}: "))
                if user_answer == answer:
                    correct += 1
                    break
                print("EEE")
                attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1

        print(f"{x} + {y} = {answer}")

    correct = 10 - attempts
    print(f"You got: {correct}/10")


if __name__ == "__main__":
    main()
