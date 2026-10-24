"""Шаблонний метод: базовий клас задає кістяк алгоритму."""
from abc import ABC, abstractmethod
class DataExporter(ABC):
    def export(self, data): return self.open() + " | " + self.format(data) + " | " + self.close()
    def open(self): return "Відкрито"
    @abstractmethod
    def format(self, data): pass
    def close(self): return "Закрито"
class CSVExporter(DataExporter):
    def format(self, data): return ",".join(data)
class JSONExporter(DataExporter):
    def format(self, data): return '{"items": ' + str(data) + '}'

if __name__ == "__main__":
    print(CSVExporter().export(["a", "b"]))
