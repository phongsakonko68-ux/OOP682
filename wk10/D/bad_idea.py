# DIP = Dependency Inversion Principle
# กล่าวว่า โมดูลระดับสูงไม่ควรพึ่งพาโมดูลระดับต่ำ
# BAD Idea of DIP Violation
class app:
    def __init__(self):
        self.database = MySQLDatabase()
    def save_data(self, data):
        self.database.save(data)

class MySQLDatabase:
    def save(self, data):
        print("Saving data to MySQL database:", data)

# Usage
application = app()
application.save_data("Sample Data")  # Output: Saving data to MySQL database: Sample Data