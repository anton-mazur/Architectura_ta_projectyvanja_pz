"""Будівельник: покроково складає складний об'єкт."""
from dataclasses import dataclass, field

@dataclass
class Pizza:
    size: str = "середня"
    toppings: list[str] = field(default_factory=list)
    cheese: bool = False

class PizzaBuilder:
    def __init__(self): self.pizza = Pizza()
    def with_size(self, size): self.pizza.size = size; return self
    def add_topping(self, topping): self.pizza.toppings.append(topping); return self
    def with_cheese(self): self.pizza.cheese = True; return self
    def build(self): return self.pizza

if __name__ == "__main__":
    pizza = PizzaBuilder().with_size("велика").add_topping("гриби").with_cheese().build()
    print(pizza)
