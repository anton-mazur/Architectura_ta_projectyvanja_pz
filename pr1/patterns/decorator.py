"""Декоратор: додає поведінку без зміни початкового об'єкта."""
class Coffee:
    def cost(self): return 40
    def description(self): return "Кава"
class Milk:
    def __init__(self, coffee): self.coffee = coffee
    def cost(self): return self.coffee.cost() + 15
    def description(self): return self.coffee.description() + " з молоком"
class Sugar:
    def __init__(self, coffee): self.coffee = coffee
    def cost(self): return self.coffee.cost() + 5
    def description(self): return self.coffee.description() + " з цукром"

if __name__ == "__main__":
    drink = Sugar(Milk(Coffee()))
    print(drink.description(), drink.cost())
