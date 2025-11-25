class Shape:
    def area(self):
        print("Area of the shape is not defined")


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(f"Area of Circle: {3.14 * self.r * self.r}")


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print(f"Area of Rectangle: {self.l * self.b}")


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(f"Area of Triangle: {0.5 * self.b * self.h}")


# Testing
c1 = Circle(5)
c1.area()

r1 = Rectangle(4, 6)
r1.area()

t1 = Triangle(10, 12)
t1.area()

s1 = Shape()
s1.area()
