# LSP (Liskov Substitution Principle) 
# กล่าวว่า วัตถุของซับคลาสควรจะสามารถแทนที่วัตถุของซูเปอร์คลาสได้โดยไม่ทำให้โปรแกรมทำงานผิดพลาด

# BAD Idea of LSP Violation
class Rectangle: # สี่เหลี่ยม
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(Rectangle): # สี่เหลี่ยมจัตุรัส
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, width):
        self.width = width
        self.height = width  # Violates LSP by changing height

    def set_height(self, height):
        self.height = height
        self.width = height  # Violates LSP by changing width

def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height 

rect = Rectangle(2, 3)
print("Rectangle area:", resize_rectangle(rect, 4, 5))  # Expected: 20
sq = Square(4)
print("Square area:", resize_rectangle(sq, 4, 5))  # Unexpected: 25 (should be 20)  