# The new class will be called Triangle and this is the list of our expectations: The constructor accepts three
# arguments - all of them are objects of the Point class; The points are stored inside the object; the class provides
# a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three
# points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you
# know it perfectly yourself.)

import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice_a = vertice1
        self.vertice_b = vertice2
        self.vertice_c = vertice3

    def perimeter(self):
        distance_a_to_b = math.sqrt(math.pow(self.vertice_b.x - self.vertice_a.x, 2) + math.pow(
            self.vertice_b.y - self.vertice_a.y, 2))
        distance_a_to_c = math.sqrt(math.pow(self.vertice_c.x - self.vertice_a.x, 2) + math.pow(
            self.vertice_c.y - self.vertice_a.y, 2))
        distance_b_to_c = math.sqrt(math.pow(self.vertice_c.x - self.vertice_b.x, 2) + math.pow(
            self.vertice_c.y - self.vertice_b.y, 2))

        return distance_a_to_b + distance_a_to_c + distance_b_to_c


if __name__ == '__main__':
    triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    print(triangle.perimeter())
