"""LSP: підтипи можна підставляти замість базового типу."""
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self) -> str: pass

class Sparrow(Bird):
    def move(self): return "Горобець летить"

class Penguin(Bird):
    def move(self): return "Пінгвін пливе"

def show_movement(bird: Bird) -> None:
    print(bird.move())

if __name__ == "__main__":
    show_movement(Sparrow())
    show_movement(Penguin())
