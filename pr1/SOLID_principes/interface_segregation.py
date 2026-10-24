"""ISP: клієнти не повинні залежати від методів, які не використовують."""
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_document(self, text: str): pass

class Scannable(ABC):
    @abstractmethod
    def scan_document(self): pass

class SimplePrinter(Printable):
    def print_document(self, text): return f"Друк: {text}"

class MultifunctionPrinter(Printable, Scannable):
    def print_document(self, text): return f"Друк: {text}"
    def scan_document(self): return "Сканування завершено"

if __name__ == "__main__":
    printer = SimplePrinter()
    print(printer.print_document("Заява"))
    print(MultifunctionPrinter().scan_document())
