# S = SRP = Single Responsibility Principle

# BAD Idea: A class that handles multiple responsibilities
class ReportGenerator:
    def __init__(self, data):
        self.dat = data
    
    def generate_pdf(self):
        # Code to generate PDF report
        pass

    def generate_excel(self):
        # Code to generate Excel report
        pass

    def send_email(self, recipient):
        # Code to send the report via email
        pass
