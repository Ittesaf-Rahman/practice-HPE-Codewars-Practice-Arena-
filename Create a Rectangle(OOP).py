class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2 * (self.height + self.width)
h = float(input("Type the height of this rectangle : "))
w = float(input("Type the width of this rectangle : "))
p = rectangle(h, w)
print(f"The area of the rectangle is {p.area()}")
print(f"The perimeter of the rectangle is {p.perimeter()} ")