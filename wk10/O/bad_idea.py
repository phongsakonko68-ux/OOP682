# Open-Closed Principle (OCP) states that software entities
# (classes, modules, functions, etc.)
# but closed for modification. This means that you should be able
# should be open for extension but closed for modification.
# This means that you should be able to add new functionality
# to a class without changing its existing code.

# BAD Idea: A class that violates the Open-Closed Principle
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius ** 2
    elif isinstance(shape, Rectangle):
        return shape.width * shape.height
    else:
        raise ValueError("Unknown shape")