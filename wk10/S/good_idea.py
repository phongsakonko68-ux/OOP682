# S = SRP = Single Responsibility Principle

# GOOD Idea: Separate classes for each responsibility
class PDFReportGenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        # Code to generate PDF report
        pass

class ExcelReportGenerator:
    def __init__(self, data):
        self.data = data
    def generate(self):
        # Code to generate Excel report
        pass

class EmailSender:
    def __init__(self, report):
        self.report = report
    def send(self, recipient):
        # Code to send the report via email
        pass