from models.Preson import Person
from models.student import Student
from models.staff import Staff

person = Person(1234567890123, "John", 30)
student = Student(1234567890123, "Alice", 20, "S123")
staff = Staff(2345678901234, "Bob", 35, "ST456")
print(person)
print(student)
print(staff)

def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}"

print(get_person_info(student))  # Returns "Name: Alice, Age: 20"
print(get_person_info(staff))    # Returns "Name: Bob, Age: 35"

class Employee:
    pass

manager = Employee()
# get_person_info(manager)  # Raises an error, as Employee does not inherit from Person
