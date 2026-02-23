# LSP (Liskov Substitution Principle) 
# กล่าวว่า วัตถุของซับคลาสควรจะสามารถแทนที่วัตถุของซูเปอร์คลาสได้โดยไม่ทำให้โปรแกรมทำงานผิดพลาด
# GOOD Idea of LSP Adherence
from abc import ABC, abstractmethod
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def resize(self, new_side):
        self.side = new_side
    def area(self):
        return self.side * self.side
def resize(Shape, new_width, new_height):
    Shape.resize(new_width, new_height)
    return Shape.area()
rect = Rectangle(2, 3)
resize(rect, 4, 5)  # Works as expected
print("Rectangle area:", rect.area())  # Expected: 20
sq = Square(3)
resize(Shape, 4,5)  # Works as expected
print("Square area:", sq.area())  # Expected: 16