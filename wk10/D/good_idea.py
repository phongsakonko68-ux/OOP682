# DIP = Dependency Inversion Principle
# กล่าวว่า โมดูลระดับสูงไม่ควรพึ่งพาโมดูลระดับต่ำ
# GOOD Idea of DIP Violation
from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass
class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database:", data)
class PostgreSQLDatabase(Database):
    def save(self, data):
        print("Saving data to PostgreSQL database:", data)
class App:
    def __init__(self, database: Database):
        self.database = database
    def save_data(self, data):
        self.database.save(data)