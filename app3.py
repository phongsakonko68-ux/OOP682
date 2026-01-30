from models.classroom import ClassRoom
from models.student import Student 


oop = ClassRoom("OOP ")
oop.add_student(Student(1,"Alice", 20, "A200"))
oop.add_student(Student(2,"Bob", 22, "B201"))
print(f'จำนวนนักศึกษาที่ลงทะเบียน {oop.name} {len(oop)}')
oop.add_student(Student(3,"Charlie", 21, "C202"))
print(len(oop))
print("รายชื่อนักศึกษาที่ลงทะเบียน:")
for i in range(len(oop)):
    print(oop[i])
    