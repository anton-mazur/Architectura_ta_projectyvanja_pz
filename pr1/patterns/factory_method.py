"""Фабричний метод: підкласи обирають конкретний продукт."""
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self): pass

class Truck(Transport):
    def deliver(self): return "Доставка вантажівкою"

class Ship(Transport):
    def deliver(self): return "Доставка кораблем"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self): pass
    def plan_delivery(self): return self.create_transport().deliver()

class RoadLogistics(Logistics):
    def create_transport(self): return Truck()

class SeaLogistics(Logistics):
    def create_transport(self): return Ship()

if __name__ == "__main__":
    print(RoadLogistics().plan_delivery())
    print(SeaLogistics().plan_delivery())
