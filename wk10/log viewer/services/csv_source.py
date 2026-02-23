import csv
from interfaces.data_source import ILogSource

class CsvLogSource(ILogSource):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_logs(self):
        logs = []
        with open(self.file_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                logs.append(" | ".join(row))
        return logs