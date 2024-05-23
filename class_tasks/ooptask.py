class Cube:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        return self.x * self.x

    def surfarea(self):
        return self.x * self.x * 6

    def volume(self):
        return self.x * self.x * self.x


class Sphere:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z

    def area(self, pi=3.14):
        return pi * self.x * self.x

    def perimeter(self, pi=3.14):
        return pi * 2 * self.x

    def volume(self, pi=3.14):
        return 4 / 3 * pi * self.x * self.x * self.x

    def surfarea(self, pi=3.14):
        return 4 * pi * self.x * self.x


class Pyramid:
    def __init__(self, colour, x, y, z):
        self.colour = colour
        self.x = x
        self.y = y
        self.z = z

    def perimeter(self):
        return self.x + self.y + self.z

    def area(self):
        return 0.5 * self.x * self.y

    def volume(self):
        return 1 / 3 * self.x * self.y * self.z


sphere = Sphere("Red", 6, 8, 4)
print(sphere.area())
