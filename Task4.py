import random


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_circumference(self):
        return 2 * (3.14 * self.radius)

if __name__ == '__main__':
    rectangle = Rectangle(random.randint(1,100), random.randint(1,100))
    circle = Circle(random.randint(1,100))
    print(f"Прямокутник зі сторонами {rectangle.length} і {rectangle.width}.")
    print("Площа прямокутника: ", rectangle.get_area())
    print("Периметр прямокутника: ", rectangle.get_perimeter())

    print(f"Коло з радіусом {circle.radius}")
    print("Площа кола: ", circle.get_area())
    print("Довжина кола: ", circle.get_circumference())