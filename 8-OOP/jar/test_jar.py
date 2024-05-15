from jar import Jar


def test_init(self, capacity=12):
    self.capacity = capacity
    self.cookies = 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    self.cookies += n
    if n > 12:
        raise ValueError("Too many cookies")
    return n


def test_withdraw():
    self.cookies -= n
    if n < 0:
        raise ValueError("No cookies in jar")
    return n
