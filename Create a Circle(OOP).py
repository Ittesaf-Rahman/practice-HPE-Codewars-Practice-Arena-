import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def circumference(self):
        return 2 * math.pi * self.radius
r = float(input("Enter a number : "))
p = circle(r)
print(f"The area of this circle is : {p.area()}")
print(f"The circumference of this circle is : {p.circumference()}")