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


class Sphere(Shape):
    def __init__(self, colour, x, y, z):
    super().__init__(self,colour, x, y ,z )

    def area(self, pi=3.14):
        return pi * self.x * self.x

    def perimeter(self, pi=3.14):
        return pi * 2 * self.x

    def volume(self, pi=3.14):
        return 4 / 3 * pi * self.x * self.x * self.x

    def surfarea(self, pi=3.14):
        return 4 * pi * self.x * self.x


sphere = Sphere("Red", 6, 8, 4)
print(sphere.area())
