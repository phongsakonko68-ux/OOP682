# ISP = Interface Segregation Principle 
# กล่าวว่า ลูกค้าควรจะไม่ถูกบังคับให้พึ่งพาอินเทอร์เฟซที่พวกเขาไม่ได้ใช้

# GOOD Idea of ISP Violation
from abc import ABC, abstractmethod

class Printer:
    @abstractmethod
    def print(self, document):
        pass
class Scanner:
    @abstractmethod
    def scan(self, document):
        pass
class Fax:
    @abstractmethod
    def fax(self, document):
        pass
class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document):
        print("Printing document.....")
    def scan(self, document):
        print("Scanning document.....")
    def fax(self, document):
        print("Faxing document.....")