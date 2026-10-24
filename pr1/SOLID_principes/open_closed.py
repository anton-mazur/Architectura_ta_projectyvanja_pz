"""OCP: система відкрита для розширення, але закрита для зміни."""
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: pass

class RegularDiscount(Discount):
    def apply(self, price): return price

class StudentDiscount(Discount):
    def apply(self, price): return price * 0.8

class HolidayDiscount(Discount):
    def apply(self, price): return price * 0.7

class Checkout:
    def total(self, price: float, discount: Discount) -> float:
        return discount.apply(price)

if __name__ == "__main__":
    checkout = Checkout()
    print(checkout.total(1_000, StudentDiscount()))
    print(checkout.total(1_000, HolidayDiscount()))
