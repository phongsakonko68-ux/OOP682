from models.Preson import Person


class Staff(Person):
    def __init__(self, pid, name, age,Staff_id):
        super().__init__(pid, name, age)
        self.Staff_id = Staff_id

    def __str__(self):
        return f"Staff ID: {self.Staff_id}, Name: {self.name}, Age: {self.age}"