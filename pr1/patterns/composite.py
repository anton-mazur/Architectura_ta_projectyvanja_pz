"""Компонувальник: однаково працює з листками та групами."""
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def total(self): pass
class Product(Component):
    def __init__(self, name, price): self.name, self.price = name, price
    def total(self): return self.price
class Box(Component):
    def __init__(self): self.items = []
    def add(self, item): self.items.append(item)
    def total(self): return sum(item.total() for item in self.items)

if __name__ == "__main__":
    order = Box(); order.add(Product("Книга", 300)); order.add(Product("Ручка", 25))
    print(order.total())
