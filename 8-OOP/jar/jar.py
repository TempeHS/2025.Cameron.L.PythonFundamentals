from jar import Jar

class Jar:
    def __init__(self, capacity=12):
    if capacity < 0: 
		raise ValueError
    def __str__(self):


    def deposit(self, n):

    def withdraw(self, n):

    @property
    def capacity(self):


    @property
    def size(self):


    def test_init():
    


def test_str():
	jar = Jar()
	assert str(jar) == ""
	jar.deposit(1)
	assert str(jar) == "🍪"
	jar.deposit(11)
	assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
	...


def test_withdraw():
	...