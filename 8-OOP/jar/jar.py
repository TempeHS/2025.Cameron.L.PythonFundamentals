class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.cookies * "🍪"

    def deposit(self, n):
        self.cookies += n
        if n > 12:
            raise ValueError("Too many cookies")
        return n

    def withdraw(self, n):
        self.cookies -= n
        if n < 0:
            raise ValueError("No cookies in jar")
        return n

    def capacity(self):
        return self.cookies

    def size(self):
        return self.cookies


def main():

    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()
