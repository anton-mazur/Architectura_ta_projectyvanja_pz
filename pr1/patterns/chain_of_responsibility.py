"""Ланцюжок обов'язків: запит передається наступному обробнику."""
class Handler:
    def __init__(self, successor=None): self.successor = successor
    def handle(self, amount):
        if self.successor: return self.successor.handle(amount)
        return "Немає погоджувача"
class Manager(Handler):
    def handle(self, amount):
        return "Менеджер погодив" if amount <= 1_000 else super().handle(amount)
class Director(Handler):
    def handle(self, amount):
        return "Директор погодив" if amount <= 10_000 else super().handle(amount)

if __name__ == "__main__":
    print(Manager(Director()).handle(5_000))
