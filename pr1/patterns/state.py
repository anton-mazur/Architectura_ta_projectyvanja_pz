"""Стан: поведінка об'єкта змінюється залежно від поточного стану."""
class TrafficLight:
    def __init__(self): self.state = Red()
    def next(self): self.state = self.state.next(); return self.state.name
class Red:
    name = "Червоний"
    def next(self): return Green()
class Green:
    name = "Зелений"
    def next(self): return Yellow()
class Yellow:
    name = "Жовтий"
    def next(self): return Red()

if __name__ == "__main__":
    light = TrafficLight()
    print(light.next(), light.next(), light.next())
