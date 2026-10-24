"""Стратегія: дозволяє змінювати алгоритм під час виконання."""
class PriceCalculator:
    def __init__(self, discount): self.discount = discount
    def total(self, price): return self.discount(price)
def no_discount(price): return price
def student_discount(price): return price * 0.8

if __name__ == "__main__":
    calculator = PriceCalculator(no_discount)
    print(calculator.total(100))
    calculator.discount = student_discount
    print(calculator.total(100))
