class Point:
    def __init__(self, coordinate_x=0, coordinate_y=0, color="Black"):
        self.x = coordinate_x
        self.y = coordinate_y
        self.color = color

if __name__ == '__main__':
    points = []
    for i in range(1000):
        point = Point(color="red")
        points.append(point)

    print("Кількість елементів у списку points: ", len(points))

    points[2].coordinate_x = 10
    print(f"Змінена координата x третьої точки: {points[2].coordinate_x}")