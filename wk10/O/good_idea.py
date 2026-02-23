# Open-Closed Principle (OCP) states that software entities
# (classes, modules, functions, etc.)
# but closed for modification. This means that you should be able
# should be open for extension but closed for modification.
# This means that you should be able to add new functionality
# to a class without changing its existing code.

# GOOD Idea: A class of OCP Adherence
from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
            raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
         self.width = width
         self.height = height
    def area(self):
        return self.width * self.height0
def calculate_area(shape):
    return shape.area()