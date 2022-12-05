from abc import ABC, abstractmethod


class Polygon(ABC):
    no_of_polygons = 0

    def __init__(self):
        self.polygon_id = Polygon.no_of_polygons
        Polygon.no_of_polygons += 1

    def __str__(self):
        return f"There are {self.no_of_polygons} created"

    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

    
class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):
    # custom
    def noofsides(self):
        print("I have six sides")


triangle = Triangle()
triangle.noofsides()

triangle_two = Triangle()
triangle_two.noofsides()

hexagon = Hexagon()
hexagon.noofsides()

print(triangle.no_of_polygons)
print(triangle_two.no_of_polygons)
print(hexagon.no_of_polygons)

print(triangle.polygon_id)
print(triangle_two.polygon_id)
print(hexagon.polygon_id)