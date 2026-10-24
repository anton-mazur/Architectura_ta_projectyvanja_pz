"""Міст: відокремлює абстракцію пристрою від його реалізації."""
from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def set_volume(self, value): pass
class TV(Device):
    def set_volume(self, value): return f"TV: гучність {value}"
class Radio(Device):
    def set_volume(self, value): return f"Radio: гучність {value}"
class Remote:
    def __init__(self, device): self.device = device
    def volume_up(self): return self.device.set_volume(10)

if __name__ == "__main__":
    print(Remote(Radio()).volume_up())
