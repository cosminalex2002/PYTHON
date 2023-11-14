import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        super().__init__()
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def area(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

    def perimeter(self):
        return self.l1 + self.l2 + self.l3

circle = Circle(radius=5)
print(f"Cerc : Ariue: {circle.area()}, Perim: {circle.perimeter()}")

rectangle = Rectangle(length=4, width=6)
print(f"Dreptunghi : Ariue: {rectangle.area()}, Perim: {rectangle.perimeter()}")

triangle = Triangle(l1=3, l2=4, l3=5)
print(f"Triunghi : Ariue: {triangle.area()}, Perim: {triangle.perimeter()}")
