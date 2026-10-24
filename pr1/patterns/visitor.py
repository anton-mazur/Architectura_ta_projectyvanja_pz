"""Відвідувач: додає операції до класів без їх зміни."""
class Circle:
    def __init__(self, radius): self.radius = radius
    def accept(self, visitor): return visitor.visit_circle(self)
class Rectangle:
    def __init__(self, width, height): self.width, self.height = width, height
    def accept(self, visitor): return visitor.visit_rectangle(self)
class AreaVisitor:
    def visit_circle(self, circle): return 3.14159 * circle.radius ** 2
    def visit_rectangle(self, rectangle): return rectangle.width * rectangle.height

if __name__ == "__main__":
    visitor = AreaVisitor()
    print(Circle(2).accept(visitor), Rectangle(3, 4).accept(visitor))
