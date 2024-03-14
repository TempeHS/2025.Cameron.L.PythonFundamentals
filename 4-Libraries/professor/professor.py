import random


def main():
    X = int
    Y = int
    X, Y = X + Y


def get_level():
    user_input = int(input("Level:"))
    level = random.randint(1, 3)


def generate_integer(level):
    if 1 > get_level > 3:
        print("Invalid")
    raise ValueError


if __name__ == "__main__":
    main()
